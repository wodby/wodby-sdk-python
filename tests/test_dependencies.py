"""Exercise the generated client against a local server, without API credentials."""
import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import wodby
from wodby.rest import ApiException


class Handler(BaseHTTPRequestHandler):
    requests = []

    def log_message(self, *args):
        pass

    def respond(self, code, data):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('X-Test', 'response-header')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        self.requests.append((self.path, self.headers, None))
        if self.path == '/orgs':
            self.respond(200, [{'id': 'org-1', 'title': 'Example', 'name': 'example', 'status': 'ok', 'created': 1, 'updated': 1}])
        else:
            self.respond(403, {'message': 'Forbidden'})

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
        self.requests.append((self.path, self.headers, body))
        self.respond(200, {'task': {'id': 'task-1', 'title': 'Deploy', 'org_id': 'org-1', 'status': 'done', 'ttl': 60, 'created': 1, 'updated': 1}})


class DependencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_requests_responses_and_errors(self):
        config = wodby.Configuration()
        config.host = 'http://127.0.0.1:%d' % self.server.server_port
        config.api_key['X-API-KEY'] = 'test-key'
        client = wodby.ApiClient(config)
        orgs = wodby.OrganizationApi(client)
        self.assertEqual(orgs.get_orgs()[0].id, 'org-1')
        self.assertEqual(Handler.requests[-1][1]['X-API-KEY'], 'test-key')
        result = wodby.InstanceApi(client).deploy_instance('instance-1', data=wodby.RequestInstanceDeploy(post_deployment=True), async_req=True).get()
        self.assertEqual(result.task.id, 'task-1')
        self.assertEqual(Handler.requests[-1][2], {'post_deployment': True})
        with self.assertRaises(ApiException) as caught:
            orgs.get_org('missing')
        self.assertEqual(caught.exception.status, 403)
        self.assertEqual(caught.exception.headers['X-Test'], 'response-header')
        raw = client.rest_client.GET(config.host + '/orgs')
        self.assertEqual(raw.getheader('X-Test'), 'response-header')
        self.assertEqual(raw.getheaders()['X-Test'], 'response-header')
