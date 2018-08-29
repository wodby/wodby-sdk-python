# wodby_sdk.DomainApi

All URIs are relative to *https://api.wodby.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_domain**](DomainApi.md#get_domain) | **GET** /domains/{id} | 
[**get_domains**](DomainApi.md#get_domains) | **GET** /domains | 


# **get_domain**
> Domain get_domain(id)



Retrieve domain

### Example
```python
from __future__ import print_function
import time
import wodby_sdk
from wodby_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = wodby_sdk.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = wodby_sdk.DomainApi(wodby_sdk.ApiClient(configuration))
id = 'id_example' # str | Domain ID

try:
    api_response = api_instance.get_domain(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->get_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Domain ID | 

### Return type

[**Domain**](Domain.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domains**
> list[Domain] get_domains(org_id=org_id, instance_id=instance_id, server_id=server_id, status=status, type=type, name=name)



Retrieve domains

### Example
```python
from __future__ import print_function
import time
import wodby_sdk
from wodby_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = wodby_sdk.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = wodby_sdk.DomainApi(wodby_sdk.ApiClient(configuration))
org_id = 'org_id_example' # str | Organization ID (optional)
instance_id = 'instance_id_example' # str | Instance ID (optional)
server_id = 'server_id_example' # str | Server ID (optional)
status = 'status_example' # str | Domain status (optional)
type = 'type_example' # str | Domain type (optional)
name = 'name_example' # str | Domain name (optional)

try:
    api_response = api_instance.get_domains(org_id=org_id, instance_id=instance_id, server_id=server_id, status=status, type=type, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->get_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | [**str**](.md)| Organization ID | [optional] 
 **instance_id** | [**str**](.md)| Instance ID | [optional] 
 **server_id** | [**str**](.md)| Server ID | [optional] 
 **status** | **str**| Domain status | [optional] 
 **type** | **str**| Domain type | [optional] 
 **name** | **str**| Domain name | [optional] 

### Return type

[**list[Domain]**](Domain.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

