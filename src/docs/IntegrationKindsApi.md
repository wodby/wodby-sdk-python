# wodby.IntegrationKindsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integration_kinds_id_database_machine_types_get**](IntegrationKindsApi.md#integration_kinds_id_database_machine_types_get) | **GET** /integration-kinds/{id}/database-machine-types | List database machine types
[**integration_kinds_id_database_regions_get**](IntegrationKindsApi.md#integration_kinds_id_database_regions_get) | **GET** /integration-kinds/{id}/database-regions | List database regions
[**integration_kinds_id_database_settings_get**](IntegrationKindsApi.md#integration_kinds_id_database_settings_get) | **GET** /integration-kinds/{id}/database-settings | Get database settings
[**integration_kinds_id_database_types_get**](IntegrationKindsApi.md#integration_kinds_id_database_types_get) | **GET** /integration-kinds/{id}/database-types | List database types
[**integration_kinds_id_database_versions_get**](IntegrationKindsApi.md#integration_kinds_id_database_versions_get) | **GET** /integration-kinds/{id}/database-versions | List database versions


# **integration_kinds_id_database_machine_types_get**
> List[Dict[str, object]] integration_kinds_id_database_machine_types_get(id, db_type, version, ha=ha, region=region, zone=zone)

List database machine types

### Example

* Api Key Authentication (accessTokenHeader):
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

# Configure API key authorization: accessTokenHeader
configuration.api_key['accessTokenHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenHeader'] = 'Bearer'

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
        api_response = api_instance.integration_kinds_id_database_machine_types_get(id, db_type, version, ha=ha, region=region, zone=zone)
        print("The response of IntegrationKindsApi->integration_kinds_id_database_machine_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationKindsApi->integration_kinds_id_database_machine_types_get: %s\n" % e)
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

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Database machine types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integration_kinds_id_database_regions_get**
> List[Dict[str, object]] integration_kinds_id_database_regions_get(id, db_type, version, ha=ha)

List database regions

### Example

* Api Key Authentication (accessTokenHeader):
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

# Configure API key authorization: accessTokenHeader
configuration.api_key['accessTokenHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenHeader'] = 'Bearer'

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
        api_response = api_instance.integration_kinds_id_database_regions_get(id, db_type, version, ha=ha)
        print("The response of IntegrationKindsApi->integration_kinds_id_database_regions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationKindsApi->integration_kinds_id_database_regions_get: %s\n" % e)
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

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Database regions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integration_kinds_id_database_settings_get**
> Dict[str, object] integration_kinds_id_database_settings_get(id, db_type)

Get database settings

### Example

* Api Key Authentication (accessTokenHeader):
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

# Configure API key authorization: accessTokenHeader
configuration.api_key['accessTokenHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenHeader'] = 'Bearer'

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
        api_response = api_instance.integration_kinds_id_database_settings_get(id, db_type)
        print("The response of IntegrationKindsApi->integration_kinds_id_database_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationKindsApi->integration_kinds_id_database_settings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **db_type** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Database settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integration_kinds_id_database_types_get**
> List[DatabaseType] integration_kinds_id_database_types_get(id)

List database types

### Example

* Api Key Authentication (accessTokenHeader):
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

# Configure API key authorization: accessTokenHeader
configuration.api_key['accessTokenHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenHeader'] = 'Bearer'

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
        api_response = api_instance.integration_kinds_id_database_types_get(id)
        print("The response of IntegrationKindsApi->integration_kinds_id_database_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationKindsApi->integration_kinds_id_database_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[DatabaseType]**](DatabaseType.md)

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Database types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integration_kinds_id_database_versions_get**
> List[DatabaseVersion] integration_kinds_id_database_versions_get(id, db_type)

List database versions

### Example

* Api Key Authentication (accessTokenHeader):
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

# Configure API key authorization: accessTokenHeader
configuration.api_key['accessTokenHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenHeader'] = 'Bearer'

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
        api_response = api_instance.integration_kinds_id_database_versions_get(id, db_type)
        print("The response of IntegrationKindsApi->integration_kinds_id_database_versions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationKindsApi->integration_kinds_id_database_versions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **db_type** | **str**|  | 

### Return type

[**List[DatabaseVersion]**](DatabaseVersion.md)

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Database versions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

