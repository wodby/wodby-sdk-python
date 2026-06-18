# wodby.ImportsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_import**](ImportsApi.md#create_import) | **POST** /imports | Create import
[**get_import**](ImportsApi.md#get_import) | **GET** /imports/{id} | Get import
[**list_imports**](ImportsApi.md#list_imports) | **GET** /imports | List imports


# **create_import**
> OperationResult create_import(new_import_input)

Create import

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.new_import_input import NewImportInput
from wodby.models.operation_result import OperationResult
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ImportsApi(api_client)
    new_import_input = wodby.NewImportInput() # NewImportInput | 

    try:
        # Create import
        api_response = api_instance.create_import(new_import_input)
        print("The response of ImportsApi->create_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportsApi->create_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_import_input** | [**NewImportInput**](NewImportInput.md)|  | 

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Import task result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import**
> ModelImport get_import(id)

Get import

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.model_import import ModelImport
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ImportsApi(api_client)
    id = 56 # int | 

    try:
        # Get import
        api_response = api_instance.get_import(id)
        print("The response of ImportsApi->get_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportsApi->get_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Import |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_imports**
> List[ModelImport] list_imports(app_instance_id=app_instance_id, app_service_id=app_service_id, database_id=database_id, database_db_id=database_db_id)

List imports

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.model_import import ModelImport
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ImportsApi(api_client)
    app_instance_id = 56 # int |  (optional)
    app_service_id = 56 # int |  (optional)
    database_id = 56 # int |  (optional)
    database_db_id = 56 # int |  (optional)

    try:
        # List imports
        api_response = api_instance.list_imports(app_instance_id=app_instance_id, app_service_id=app_service_id, database_id=database_id, database_db_id=database_db_id)
        print("The response of ImportsApi->list_imports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportsApi->list_imports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_instance_id** | **int**|  | [optional] 
 **app_service_id** | **int**|  | [optional] 
 **database_id** | **int**|  | [optional] 
 **database_db_id** | **int**|  | [optional] 

### Return type

[**List[ModelImport]**](ModelImport.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of imports |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

