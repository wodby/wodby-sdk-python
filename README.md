# Wodby 2.0 SDK for Python

Python client for the Wodby 2.0 Public API.

## Documentation

- [API reference](https://wodby.com/docs/2.0/api/)
- [OpenAPI schema](https://wodby.com/docs/2.0/api/openapi.yaml)
- Generated SDK docs: `src/docs`

## Install

```bash
pip install wodby
```

## Authentication

Wodby API requests use an API key in the `X-API-KEY` header.

```python
import os
import wodby

configuration = wodby.Configuration()
configuration.api_key["X-API-KEY"] = os.environ["WODBY_API_KEY"]
```
