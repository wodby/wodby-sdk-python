# wodby.IntegrationKindsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_integration_kind_database_settings**](IntegrationKindsApi.md#get_integration_kind_database_settings) | **GET** /integration-kinds/{id}/database-settings | Get database settings
[**list_integration_kind_database_machine_types**](IntegrationKindsApi.md#list_integration_kind_database_machine_types) | **GET** /integration-kinds/{id}/database-machine-types | List database machine types
[**list_integration_kind_database_regions**](IntegrationKindsApi.md#list_integration_kind_database_regions) | **GET** /integration-kinds/{id}/database-regions | List database regions
[**list_integration_kind_database_types**](IntegrationKindsApi.md#list_integration_kind_database_types) | **GET** /integration-kinds/{id}/database-types | List database types
[**list_integration_kind_database_versions**](IntegrationKindsApi.md#list_integration_kind_database_versions) | **GET** /integration-kinds/{id}/database-versions | List database versions


# **get_integration_kind_database_settings**
> Dict[str, object] get_integration_kind_database_settings(id, db_type)

Get database settings

Returns the database settings identified by the request path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
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
    api_instance = wodby.IntegrationKindsApi(api_client)
    id = 56 # int | 
    db_type = 'db_type_example' # str | 

    try:
        # Get database settings
        api_response = api_instance.get_integration_kind_database_settings(id, db_type)
        print("The response of IntegrationKindsApi->get_integration_kind_database_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationKindsApi->get_integration_kind_database_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **db_type** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Database settings |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integration_kind_database_machine_types**
> List[Dict[str, object]] list_integration_kind_database_machine_types(id, db_type, version, ha=ha, region=region, zone=zone)

List database machine types

Returns database machine types matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
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
    api_instance = wodby.IntegrationKindsApi(api_client)
    id = 56 # int | 
    db_type = 'db_type_example' # str | 
    version = 'version_example' # str | 
    ha = False # bool |  (optional) (default to False)
    region = 'region_example' # str |  (optional)
    zone = 'zone_example' # str |  (optional)

    try:
        # List database machine types
        api_response = api_instance.list_integration_kind_database_machine_types(id, db_type, version, ha=ha, region=region, zone=zone)
        print("The response of IntegrationKindsApi->list_integration_kind_database_machine_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationKindsApi->list_integration_kind_database_machine_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **db_type** | **str**|  | 
 **version** | **str**|  | 
 **ha** | **bool**|  | [optional] [default to False]
 **region** | **str**|  | [optional] 
 **zone** | **str**|  | [optional] 

### Return type

**List[Dict[str, object]]**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Database machine types |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integration_kind_database_regions**
> List[Dict[str, object]] list_integration_kind_database_regions(id, db_type, version, ha=ha)

List database regions

Returns database regions matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
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
    api_instance = wodby.IntegrationKindsApi(api_client)
    id = 56 # int | 
    db_type = 'db_type_example' # str | 
    version = 'version_example' # str | 
    ha = False # bool |  (optional) (default to False)

    try:
        # List database regions
        api_response = api_instance.list_integration_kind_database_regions(id, db_type, version, ha=ha)
        print("The response of IntegrationKindsApi->list_integration_kind_database_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationKindsApi->list_integration_kind_database_regions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **db_type** | **str**|  | 
 **version** | **str**|  | 
 **ha** | **bool**|  | [optional] [default to False]

### Return type

**List[Dict[str, object]]**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Database regions |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integration_kind_database_types**
> List[DatabaseType] list_integration_kind_database_types(id)

List database types

Returns database types matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.database_type import DatabaseType
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
    api_instance = wodby.IntegrationKindsApi(api_client)
    id = 56 # int | 

    try:
        # List database types
        api_response = api_instance.list_integration_kind_database_types(id)
        print("The response of IntegrationKindsApi->list_integration_kind_database_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationKindsApi->list_integration_kind_database_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[DatabaseType]**](DatabaseType.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Database types |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integration_kind_database_versions**
> List[DatabaseVersion] list_integration_kind_database_versions(id, db_type)

List database versions

Returns database versions matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.database_version import DatabaseVersion
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
    api_instance = wodby.IntegrationKindsApi(api_client)
    id = 56 # int | 
    db_type = 'db_type_example' # str | 

    try:
        # List database versions
        api_response = api_instance.list_integration_kind_database_versions(id, db_type)
        print("The response of IntegrationKindsApi->list_integration_kind_database_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationKindsApi->list_integration_kind_database_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **db_type** | **str**|  | 

### Return type

[**List[DatabaseVersion]**](DatabaseVersion.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Database versions |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

