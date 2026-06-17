# Wodby SDK for Python

Python client for the Wodby Public API.

This repository is generated from the OpenAPI 3 schema maintained in
[`wodby/backend-api`](https://github.com/wodby/backend-api). The `2.0` branch is
updated by the backend API release pipeline.

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

## Regenerate

The backend API pipeline copies `swagger.json` into this repository and runs:

```bash
make build
```

This uses `openapitools/openapi-generator-cli:v7.10.0` and writes generated code
to `src`.
