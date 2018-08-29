# wodby_sdk.ServerApi

All URIs are relative to *https://api.wodby.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_server**](ServerApi.md#get_server) | **GET** /servers/{id} | 
[**get_servers**](ServerApi.md#get_servers) | **GET** /servers | 


# **get_server**
> Server get_server(id)



Retrieve server

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
api_instance = wodby_sdk.ServerApi(wodby_sdk.ApiClient(configuration))
id = 'id_example' # str | Server ID

try:
    api_response = api_instance.get_server(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->get_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Server ID | 

### Return type

[**Server**](Server.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_servers**
> list[Server] get_servers(org_id=org_id, name=name)



Retrieve servers

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
api_instance = wodby_sdk.ServerApi(wodby_sdk.ApiClient(configuration))
org_id = 'org_id_example' # str | Organization ID (optional)
name = 'name_example' # str | Server name (optional)

try:
    api_response = api_instance.get_servers(org_id=org_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->get_servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | [**str**](.md)| Organization ID | [optional] 
 **name** | **str**| Server name | [optional] 

### Return type

[**list[Server]**](Server.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

