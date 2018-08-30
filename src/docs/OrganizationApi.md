# wodby.OrganizationApi

All URIs are relative to *https://api.wodby.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_org**](OrganizationApi.md#get_org) | **GET** /orgs/{id} | 
[**get_orgs**](OrganizationApi.md#get_orgs) | **GET** /orgs | 


# **get_org**
> Org get_org(id)



Retrieve organization

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
api_instance = wodby.OrganizationApi(wodby.ApiClient(configuration))
id = 'id_example' # str | Organization ID

try:
    api_response = api_instance.get_org(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Organization ID | 

### Return type

[**Org**](Org.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orgs**
> list[Org] get_orgs(name=name)



Retrieve organizations

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
api_instance = wodby.OrganizationApi(wodby.ApiClient(configuration))
name = 'name_example' # str | Organization name (optional)

try:
    api_response = api_instance.get_orgs(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_orgs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Organization name | [optional] 

### Return type

[**list[Org]**](Org.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

