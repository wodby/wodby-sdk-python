# Wodby SDK Python

[![PyPi](https://img.shields.io/pypi/v/wodby.svg)](https://pypi.org/project/wodby/)


The Wodby SDK for Python makes it easy for developers to access Wodby in their Python code. You can get started in minutes by installing the SDK with the language package manager.

---

## Table of Contents

- [Documentation](#documentation)
- [Basic usage](#basic-usage)

## Requirements

Python 3.10 or newer, with urllib3 2.7+, current certifi, python-dateutil and six. These minimums apply to the next 3.x release; existing releases are unchanged.

SDK 3.x targets Wodby 1. SDK 4.x targets Wodby 2.

## Documentation

- [API reference](https://wodby.com/docs/1.0/api)
- [Automatically generated documentation](src/README.md)

## Basic usage

Install wodby client:
```bash
pip install "wodby>=3,<4"

```

Fetch user`s organizations:
```python
import os
import wodby
from pprint import pprint

configuration = wodby.Configuration()
configuration.api_key['X-API-KEY'] = os.environ['WODBY_API_KEY']

org_api = wodby.OrganizationApi(wodby.ApiClient(configuration))
org_api.get_orgs()
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
