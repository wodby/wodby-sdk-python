# wodby.DefaultApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_open_api_json**](DefaultApi.md#get_open_api_json) | **GET** /openapi.json | Get OpenAPI JSON
[**get_open_api_yaml**](DefaultApi.md#get_open_api_yaml) | **GET** /openapi.yaml | Get OpenAPI YAML


# **get_open_api_json**
> object get_open_api_json()

Get OpenAPI JSON

Returns the public OpenAPI schema in JSON format.

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
        api_response = api_instance.get_open_api_json()
        print("The response of DefaultApi->get_open_api_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_open_api_json: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpenAPI JSON |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_api_yaml**
> str get_open_api_yaml()

Get OpenAPI YAML

Returns the public OpenAPI schema in YAML format.

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
        api_response = api_instance.get_open_api_yaml()
        print("The response of DefaultApi->get_open_api_yaml:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_open_api_yaml: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yaml, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpenAPI YAML |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

