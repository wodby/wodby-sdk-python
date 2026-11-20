# wodby.ServerApi

All URIs are relative to *https://api.wodby.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_server**](ServerApi.md#create_server) | **POST** /servers | Create server
[**get_server**](ServerApi.md#get_server) | **GET** /servers/{id} | Retrieve server
[**get_server_integration_options**](ServerApi.md#get_server_integration_options) | **GET** /servers/integrations/{id}/options | Retrieve server integration options
[**get_server_integrations**](ServerApi.md#get_server_integrations) | **GET** /servers/integrations | Retrieve server integrations
[**get_servers**](ServerApi.md#get_servers) | **GET** /servers | Retrieve servers


# **create_server**
> ResponseTask create_server(data)

Create server

Create a server with a hosting integration, such as a connected DigitalOcean team. The integration's provider creates the machine and Wodby installs its infrastructure on it.

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
api_instance = wodby.ServerApi(wodby.ApiClient(configuration))
data = wodby.RequestServerCreate() # RequestServerCreate | 

try:
    # Create server
    api_response = api_instance.create_server(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->create_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RequestServerCreate**](RequestServerCreate.md)|  | 

### Return type

[**ResponseTask**](ResponseTask.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server**
> Server get_server(id)

Retrieve server

Retrieve server

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
api_instance = wodby.ServerApi(wodby.ApiClient(configuration))
id = 'id_example' # str | Server ID

try:
    # Retrieve server
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

# **get_server_integration_options**
> list[ServerIntegrationRegion] get_server_integration_options(id)

Retrieve server integration options

Retrieve the regions and server sizes a hosting integration offers

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
api_instance = wodby.ServerApi(wodby.ApiClient(configuration))
id = 'id_example' # str | Integration ID

try:
    # Retrieve server integration options
    api_response = api_instance.get_server_integration_options(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->get_server_integration_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Integration ID | 

### Return type

[**list[ServerIntegrationRegion]**](ServerIntegrationRegion.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_integrations**
> list[ServerIntegration] get_server_integrations(org_id)

Retrieve server integrations

Retrieve an organization's integrations that can create servers

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
api_instance = wodby.ServerApi(wodby.ApiClient(configuration))
org_id = 'org_id_example' # str | Organization ID

try:
    # Retrieve server integrations
    api_response = api_instance.get_server_integrations(org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->get_server_integrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | [**str**](.md)| Organization ID | 

### Return type

[**list[ServerIntegration]**](ServerIntegration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_servers**
> list[Server] get_servers(org_id=org_id, name=name)

Retrieve servers

Retrieve servers

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
api_instance = wodby.ServerApi(wodby.ApiClient(configuration))
org_id = 'org_id_example' # str | Organization ID (optional)
name = 'name_example' # str | Server name (optional)

try:
    # Retrieve servers
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

