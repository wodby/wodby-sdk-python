# wodby_sdk.ApplicationApi

All URIs are relative to *https://api.wodby.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app**](ApplicationApi.md#create_app) | **POST** /apps | 
[**delete_app**](ApplicationApi.md#delete_app) | **DELETE** /apps/{id} | 
[**get_app**](ApplicationApi.md#get_app) | **GET** /apps/{id} | 
[**get_apps**](ApplicationApi.md#get_apps) | **GET** /apps | 


# **create_app**
> ResponseTaskApp create_app(data)



Create application

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
api_instance = wodby_sdk.ApplicationApi(wodby_sdk.ApiClient(configuration))
data = wodby_sdk.RequestAppCreate() # RequestAppCreate | 

try:
    api_response = api_instance.create_app(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->create_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RequestAppCreate**](RequestAppCreate.md)|  | 

### Return type

[**ResponseTaskApp**](ResponseTaskApp.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app**
> ResponseTask delete_app(id)



Delete application

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
api_instance = wodby_sdk.ApplicationApi(wodby_sdk.ApiClient(configuration))
id = 'id_example' # str | Application ID

try:
    api_response = api_instance.delete_app(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->delete_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Application ID | 

### Return type

[**ResponseTask**](ResponseTask.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app**
> App get_app(id)



Retrieve application

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
api_instance = wodby_sdk.ApplicationApi(wodby_sdk.ApiClient(configuration))
id = 'id_example' # str | Application ID

try:
    api_response = api_instance.get_app(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Application ID | 

### Return type

[**App**](App.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_apps**
> list[App] get_apps(org_id=org_id, name=name)



Retrieve applications

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
api_instance = wodby_sdk.ApplicationApi(wodby_sdk.ApiClient(configuration))
org_id = 'org_id_example' # str | Organization ID (optional)
name = 'name_example' # str | Application name (optional)

try:
    api_response = api_instance.get_apps(org_id=org_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | [**str**](.md)| Organization ID | [optional] 
 **name** | **str**| Application name | [optional] 

### Return type

[**list[App]**](App.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

