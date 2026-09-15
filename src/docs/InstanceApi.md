# wodby.InstanceApi

All URIs are relative to *https://api.wodby.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_instance**](InstanceApi.md#create_instance) | **POST** /instances | Create instance
[**delete_instance**](InstanceApi.md#delete_instance) | **DELETE** /instances/{id} | Delete application instance
[**deploy_instance**](InstanceApi.md#deploy_instance) | **POST** /instances/{id}/deploy | Deploy instance
[**deploy_instance_codebase**](InstanceApi.md#deploy_instance_codebase) | **POST** /instances/{id}/deploy-codebase | Deploy instance codebase
[**get_instance**](InstanceApi.md#get_instance) | **GET** /instances/{id} | Retrieve application instance
[**get_instances**](InstanceApi.md#get_instances) | **GET** /instances | Retrieve instances
[**upgrade_instance**](InstanceApi.md#upgrade_instance) | **POST** /instances/{id}/upgrade | Upgrade instance
[**upgrade_instances**](InstanceApi.md#upgrade_instances) | **POST** /instances/upgrade | Upgrade instances


# **create_instance**
> ResponseTaskInstance create_instance(data)

Create instance

Create instance

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
api_instance = wodby.InstanceApi(wodby.ApiClient(configuration))
data = wodby.RequestInstanceCreate() # RequestInstanceCreate | 

try:
    # Create instance
    api_response = api_instance.create_instance(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceApi->create_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RequestInstanceCreate**](RequestInstanceCreate.md)|  | 

### Return type

[**ResponseTaskInstance**](ResponseTaskInstance.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_instance**
> ResponseTask delete_instance(id)

Delete application instance

Delete application instance

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
api_instance = wodby.InstanceApi(wodby.ApiClient(configuration))
id = 'id_example' # str | Instance ID

try:
    # Delete application instance
    api_response = api_instance.delete_instance(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceApi->delete_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Instance ID | 

### Return type

[**ResponseTask**](ResponseTask.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_instance**
> ResponseTask deploy_instance(id, data=data)

Deploy instance

Deploy instance

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
api_instance = wodby.InstanceApi(wodby.ApiClient(configuration))
id = 'id_example' # str | Instance ID
data = wodby.RequestInstanceDeploy() # RequestInstanceDeploy |  (optional)

try:
    # Deploy instance
    api_response = api_instance.deploy_instance(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceApi->deploy_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Instance ID | 
 **data** | [**RequestInstanceDeploy**](RequestInstanceDeploy.md)|  | [optional] 

### Return type

[**ResponseTask**](ResponseTask.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_instance_codebase**
> ResponseTask deploy_instance_codebase(id, data=data)

Deploy instance codebase

Deploy instance codebase

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
api_instance = wodby.InstanceApi(wodby.ApiClient(configuration))
id = 'id_example' # str | Instance ID
data = wodby.RequestInstanceDeployCodebase() # RequestInstanceDeployCodebase |  (optional)

try:
    # Deploy instance codebase
    api_response = api_instance.deploy_instance_codebase(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceApi->deploy_instance_codebase: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Instance ID | 
 **data** | [**RequestInstanceDeployCodebase**](RequestInstanceDeployCodebase.md)|  | [optional] 

### Return type

[**ResponseTask**](ResponseTask.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance**
> Instance get_instance(id)

Retrieve application instance

Retrieve application instance

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
api_instance = wodby.InstanceApi(wodby.ApiClient(configuration))
id = 'id_example' # str | Instance ID

try:
    # Retrieve application instance
    api_response = api_instance.get_instance(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceApi->get_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Instance ID | 

### Return type

[**Instance**](Instance.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instances**
> list[Instance] get_instances(org_id=org_id, server_id=server_id, app_id=app_id, type=type, name=name)

Retrieve instances

Retrieve instances

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
api_instance = wodby.InstanceApi(wodby.ApiClient(configuration))
org_id = 'org_id_example' # str | Organization ID (optional)
server_id = 'server_id_example' # str | Server ID (optional)
app_id = 'app_id_example' # str | Application ID (optional)
type = 'type_example' # str | Instance type (optional)
name = 'name_example' # str | Instance name (optional)

try:
    # Retrieve instances
    api_response = api_instance.get_instances(org_id=org_id, server_id=server_id, app_id=app_id, type=type, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceApi->get_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | [**str**](.md)| Organization ID | [optional] 
 **server_id** | [**str**](.md)| Server ID | [optional] 
 **app_id** | [**str**](.md)| Application ID | [optional] 
 **type** | **str**| Instance type | [optional] 
 **name** | **str**| Instance name | [optional] 

### Return type

[**list[Instance]**](Instance.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_instance**
> ResponseTask upgrade_instance(id)

Upgrade instance

Upgrade instance

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
api_instance = wodby.InstanceApi(wodby.ApiClient(configuration))
id = 'id_example' # str | Instance ID

try:
    # Upgrade instance
    api_response = api_instance.upgrade_instance(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceApi->upgrade_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Instance ID | 

### Return type

[**ResponseTask**](ResponseTask.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_instances**
> ResponseTask upgrade_instances(data)

Upgrade instances

Upgrade instances

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
api_instance = wodby.InstanceApi(wodby.ApiClient(configuration))
data = wodby.RequestInstancesUpgrade() # RequestInstancesUpgrade | 

try:
    # Upgrade instances
    api_response = api_instance.upgrade_instances(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceApi->upgrade_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RequestInstancesUpgrade**](RequestInstancesUpgrade.md)|  | 

### Return type

[**ResponseTask**](ResponseTask.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

