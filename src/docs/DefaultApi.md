# wodby.DefaultApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**openapi_json_get**](DefaultApi.md#openapi_json_get) | **GET** /openapi.json | Get OpenAPI JSON
[**openapi_yaml_get**](DefaultApi.md#openapi_yaml_get) | **GET** /openapi.yaml | Get OpenAPI YAML


# **openapi_json_get**
> object openapi_json_get()

Get OpenAPI JSON

### Example


```python
import wodby
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)


# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.DefaultApi(api_client)

    try:
        # Get OpenAPI JSON
        api_response = api_instance.openapi_json_get()
        print("The response of DefaultApi->openapi_json_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->openapi_json_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpenAPI JSON |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openapi_yaml_get**
> str openapi_yaml_get()

Get OpenAPI YAML

### Example


```python
import wodby
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)


# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.DefaultApi(api_client)

    try:
        # Get OpenAPI YAML
        api_response = api_instance.openapi_yaml_get()
        print("The response of DefaultApi->openapi_yaml_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->openapi_yaml_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpenAPI YAML |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

