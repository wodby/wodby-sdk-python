# Wodby 1.0 SDK for Python

[![Build](https://github.com/wodby/wodby-sdk-python/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/wodby/wodby-sdk-python/actions/workflows/build.yml?query=branch%3Amaster)

Python client for the Wodby 1.0 public API. This branch maintains SDK 3.x.

## Version compatibility

| Wodby platform | SDK version | Branch | API reference |
| --- | --- | --- | --- |
| Wodby 1.0 | 3.x | [master](https://github.com/wodby/wodby-sdk-python/tree/master) | [Wodby 1.0 API](https://wodby.com/docs/1.0/api/) |
| Wodby 2.0 | 4.x | [2.0](https://github.com/wodby/wodby-sdk-python/tree/2.0) | [Wodby 2.0 API](https://wodby.com/docs/2.0/api/) |

Choose the SDK major version for your Wodby platform. Upgrading from SDK 3.x to 4.x changes the target platform to Wodby 2.0.

## Package

- [PyPI: `wodby`](https://pypi.org/project/wodby/)
- Python import: `wodby`

The PyPI package contains both SDK version lines. Select 3.x for Wodby 1.0 using the version constraint below; an unversioned install can select the 4.x SDK for Wodby 2.0.

## Requirements

Python 3.10 or newer, with urllib3 2.7+, current certifi, python-dateutil and six. These minimums apply to the next 3.x release; existing releases are unchanged.

## Documentation

- [API reference](https://wodby.com/docs/1.0/api/)
- [Automatically generated documentation](src/README.md)

## Install

Install the Wodby 1.0 SDK from PyPI:

```bash
python -m pip install "wodby>=3,<4"
```

## Basic usage

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

## Release

An annotated `3.X.Y` tag publishes the committed SDK as the `wodby` package on PyPI and creates a GitHub Release without changing Latest. The package version must match the tag. The workflow builds and checks both a wheel and a source distribution, then runs the local request tests against the installed wheel before uploading.

Publishing uses the repository's `PYPI_TOKEN` secret and fails if it is missing. A retry skips distribution files already uploaded to PyPI. Merge release workflow changes before creating the next SDK tag; existing tags retain their original workflows.
