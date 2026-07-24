# wodby.BackupsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_backup**](BackupsApi.md#create_backup) | **POST** /backups | Create backup
[**create_backup_preset**](BackupsApi.md#create_backup_preset) | **POST** /backup-presets | Create backup preset
[**delete_backup_preset**](BackupsApi.md#delete_backup_preset) | **DELETE** /backup-presets/{id} | Delete backup preset
[**get_backup**](BackupsApi.md#get_backup) | **GET** /backups/{id} | Get backup
[**get_backup_preset**](BackupsApi.md#get_backup_preset) | **GET** /backup-presets/{id} | Get backup preset
[**list_backup_presets**](BackupsApi.md#list_backup_presets) | **GET** /backup-presets | List backup presets
[**list_backups**](BackupsApi.md#list_backups) | **GET** /backups | List backups
[**update_backup_preset**](BackupsApi.md#update_backup_preset) | **PUT** /backup-presets/{id} | Update backup preset


# **create_backup**
> OperationResult create_backup(new_backup_input)

Create backup

Creates a backup and returns the created resource.

### Example

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

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Backup task result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_backup_preset**
> BackupPreset create_backup_preset(new_backup_preset_input)

Create backup preset

Creates a manual or scheduled backup preset.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.backup_preset import BackupPreset
from wodby.models.new_backup_preset_input import NewBackupPresetInput
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
    api_instance = wodby.BackupsApi(api_client)
    new_backup_preset_input = wodby.NewBackupPresetInput() # NewBackupPresetInput | 

    try:
        # Create backup preset
        api_response = api_instance.create_backup_preset(new_backup_preset_input)
        print("The response of BackupsApi->create_backup_preset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->create_backup_preset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_backup_preset_input** | [**NewBackupPresetInput**](NewBackupPresetInput.md)|  | 

### Return type

[**BackupPreset**](BackupPreset.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created backup preset |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_backup_preset**
> OperationResult delete_backup_preset(id)

Delete backup preset

Deletes a backup preset and its schedule.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
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
    api_instance = wodby.BackupsApi(api_client)
    id = 56 # int | 

    try:
        # Delete backup preset
        api_response = api_instance.delete_backup_preset(id)
        print("The response of BackupsApi->delete_backup_preset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->delete_backup_preset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup**
> Backup get_backup(id)

Get backup

Returns the backup identified by the request path.

### Example

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

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Backup |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup_preset**
> BackupPreset get_backup_preset(id)

Get backup preset

Returns the backup preset identified by the request path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.backup_preset import BackupPreset
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
    api_instance = wodby.BackupsApi(api_client)
    id = 56 # int | 

    try:
        # Get backup preset
        api_response = api_instance.get_backup_preset(id)
        print("The response of BackupsApi->get_backup_preset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->get_backup_preset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BackupPreset**](BackupPreset.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Backup preset |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_backup_presets**
> List[BackupPreset] list_backup_presets(app_instance_id=app_instance_id, app_service_id=app_service_id, database_id=database_id, database_db_id=database_db_id, org_id=org_id, backup_name=backup_name)

List backup presets

Returns backup presets matching the request filters. At least one target filter is required for user-session requests; API-key requests default to the key's organization.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.backup_preset import BackupPreset
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
    api_instance = wodby.BackupsApi(api_client)
    app_instance_id = 56 # int |  (optional)
    app_service_id = 56 # int |  (optional)
    database_id = 56 # int |  (optional)
    database_db_id = 56 # int |  (optional)
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)
    backup_name = 'backup_name_example' # str |  (optional)

    try:
        # List backup presets
        api_response = api_instance.list_backup_presets(app_instance_id=app_instance_id, app_service_id=app_service_id, database_id=database_id, database_db_id=database_db_id, org_id=org_id, backup_name=backup_name)
        print("The response of BackupsApi->list_backup_presets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->list_backup_presets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_instance_id** | **int**|  | [optional] 
 **app_service_id** | **int**|  | [optional] 
 **database_id** | **int**|  | [optional] 
 **database_db_id** | **int**|  | [optional] 
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 
 **backup_name** | **str**|  | [optional] 

### Return type

[**List[BackupPreset]**](BackupPreset.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of backup presets |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_backups**
> List[Backup] list_backups(app_instance_id=app_instance_id, app_service_id=app_service_id, database_id=database_id, database_db_id=database_db_id, backup_name=backup_name)

List backups

Returns backups matching the request filters.

### Example

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

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of backups |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_backup_preset**
> BackupPreset update_backup_preset(id, update_backup_preset_input)

Update backup preset

Updates a backup preset's destination and schedule.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.backup_preset import BackupPreset
from wodby.models.update_backup_preset_input import UpdateBackupPresetInput
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
    api_instance = wodby.BackupsApi(api_client)
    id = 56 # int | 
    update_backup_preset_input = wodby.UpdateBackupPresetInput() # UpdateBackupPresetInput | 

    try:
        # Update backup preset
        api_response = api_instance.update_backup_preset(id, update_backup_preset_input)
        print("The response of BackupsApi->update_backup_preset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->update_backup_preset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_backup_preset_input** | [**UpdateBackupPresetInput**](UpdateBackupPresetInput.md)|  | 

### Return type

[**BackupPreset**](BackupPreset.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated backup preset |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

