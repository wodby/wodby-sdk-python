# wodby.BackupApi

All URIs are relative to *https://api.wodby.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_backup**](BackupApi.md#get_backup) | **GET** /backups/{id} | 
[**get_backups**](BackupApi.md#get_backups) | **GET** /backups | 


# **get_backup**
> Backup get_backup(id)



Retrieve backup

### Example
```python
from __future__ import print_function
import time
import wodby
from wodby.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = wodby.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = wodby.BackupApi(wodby.ApiClient(configuration))
id = 'id_example' # str | Backup ID

try:
    api_response = api_instance.get_backup(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupApi->get_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Backup ID | 

### Return type

[**Backup**](Backup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backups**
> list[Backup] get_backups(org_id=org_id, instance_id=instance_id, server_id=server_id, type=type, status=status, days=days)



Retrieve backups by instance

### Example
```python
from __future__ import print_function
import time
import wodby
from wodby.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = wodby.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = wodby.BackupApi(wodby.ApiClient(configuration))
org_id = 'org_id_example' # str | Organization ID (optional)
instance_id = 'instance_id_example' # str | Instance ID (optional)
server_id = 'server_id_example' # str | Server ID (optional)
type = 'type_example' # str | Backup type (optional)
status = 'status_example' # str | Backup status (optional)
days = 56 # int | Get backups for N days (optional)

try:
    api_response = api_instance.get_backups(org_id=org_id, instance_id=instance_id, server_id=server_id, type=type, status=status, days=days)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupApi->get_backups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | [**str**](.md)| Organization ID | [optional] 
 **instance_id** | [**str**](.md)| Instance ID | [optional] 
 **server_id** | [**str**](.md)| Server ID | [optional] 
 **type** | **str**| Backup type | [optional] 
 **status** | **str**| Backup status | [optional] 
 **days** | **int**| Get backups for N days | [optional] 

### Return type

[**list[Backup]**](Backup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

