# Wodby SDK Python

[![TravisCI](https://travis-ci.com/wodby/wodby-sdk-python.svg)](https://travis-ci.com/wodby/wodby-sdk-python)
[![PyPi](https://img.shields.io/pypi/v/wodby.svg)](https://pypi.org/project/wodby/)


The Wodby SDK for Python makes it easy for developers to access Wodby in their Python code. You can get started in minutes by installing the SDK through Composer or by downloading a single zip. 

---

## Table of Contents

- [Documentation](#documentation)
- [Basic usage](#basic-usage)

## Documentation

- [API reference](https://wodby.com/docs/api)
- [Automatically generated documentation](src/README.md)

## Basic usage

Install wodby client:
```bash
pip install wodby

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