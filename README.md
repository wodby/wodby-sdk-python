# Wodby 1.0 SDK for Python

[![Build](https://github.com/wodby/wodby-sdk-python/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/wodby/wodby-sdk-python/actions/workflows/build.yml?query=branch%3Amaster)

Python client for the Wodby 1.0 public API. This branch maintains SDK 3.x.

## Version compatibility

| Wodby platform | SDK version | Branch | API reference |
| --- | --- | --- | --- |
| Wodby 1.0 | 3.x | [master](https://github.com/wodby/wodby-sdk-python/tree/master) | [Wodby 1.0 API](https://wodby.com/docs/1.0/api/) |
| Wodby 2.0 | 4.x | [2.0](https://github.com/wodby/wodby-sdk-python/tree/2.0) | [Wodby 2.0 API](https://wodby.com/docs/2.0/api/) |

Choose the SDK major version for your Wodby platform. Upgrading from SDK 3.x to 4.x changes the target platform to Wodby 2.0.

## Requirements

Python 3.10 or newer, with urllib3 2.7+, current certifi, python-dateutil and six. These minimums apply to the next 3.x release; existing releases are unchanged.

## Documentation

- [API reference](https://wodby.com/docs/1.0/api/)
- [Automatically generated documentation](src/README.md)

## Basic usage

Install wodby client:
```bash
pip install "wodby>=3,<4"
```

Fetch the user's organizations:
```python
import os
import wodby

configuration = wodby.Configuration()
configuration.api_key['X-API-KEY'] = os.environ['WODBY_API_KEY']

org_api = wodby.OrganizationApi(wodby.ApiClient(configuration))
print(org_api.get_orgs())
```

## Development

```sh
python -m pip install ./src -r requirements-dev.txt
./pkg-test.sh
python -m build ./src
python -m pip_audit -r requirements.txt
```

Tests use mocks or a local HTTP server and do not require an API key.

Regenerate with `./pkg-build.sh` (Docker and Java 17 image required). The existing Swagger generator stays pinned to preserve the client API; the post-generation script reapplies modern dependency compatibility.
