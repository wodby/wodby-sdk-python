# wodby.BackupsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_backup**](BackupsApi.md#create_backup) | **POST** /backups | Create backup
[**get_backup**](BackupsApi.md#get_backup) | **GET** /backups/{id} | Get backup
[**list_backups**](BackupsApi.md#list_backups) | **GET** /backups | List backups


# **create_backup**
> OperationResult create_backup(new_backup_input)

Create backup

### Example

* Api Key Authentication (accessTokenHeader):
* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.new_backup_input import NewBackupInput
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
    api_instance = wodby.BackupsApi(api_client)
    new_backup_input = wodby.NewBackupInput() # NewBackupInput | 

    try:
        # Create backup
        api_response = api_instance.create_backup(new_backup_input)
        print("The response of BackupsApi->create_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->create_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_backup_input** | [**NewBackupInput**](NewBackupInput.md)|  | 

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Backup task result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup**
> Backup get_backup(id)

Get backup

### Example

* Api Key Authentication (accessTokenHeader):
* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.backup import Backup
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
    api_instance = wodby.BackupsApi(api_client)
    id = 56 # int | 

    try:
        # Get backup
        api_response = api_instance.get_backup(id)
        print("The response of BackupsApi->get_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->get_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Backup**](Backup.md)

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Backup |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_backups**
> List[Backup] list_backups(app_instance_id=app_instance_id, app_service_id=app_service_id, database_id=database_id, database_db_id=database_db_id, backup_name=backup_name)

List backups

### Example

* Api Key Authentication (accessTokenHeader):
* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.backup import Backup
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
    api_instance = wodby.BackupsApi(api_client)
    app_instance_id = 56 # int |  (optional)
    app_service_id = 56 # int |  (optional)
    database_id = 56 # int |  (optional)
    database_db_id = 56 # int |  (optional)
    backup_name = 'backup_name_example' # str |  (optional)

    try:
        # List backups
        api_response = api_instance.list_backups(app_instance_id=app_instance_id, app_service_id=app_service_id, database_id=database_id, database_db_id=database_db_id, backup_name=backup_name)
        print("The response of BackupsApi->list_backups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->list_backups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_instance_id** | **int**|  | [optional] 
 **app_service_id** | **int**|  | [optional] 
 **database_id** | **int**|  | [optional] 
 **database_db_id** | **int**|  | [optional] 
 **backup_name** | **str**|  | [optional] 

### Return type

[**List[Backup]**](Backup.md)

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of backups |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

