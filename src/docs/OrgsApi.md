# wodby.OrgsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_org**](OrgsApi.md#get_org) | **GET** /orgs/{id} | Get org
[**get_org_subscription**](OrgsApi.md#get_org_subscription) | **GET** /orgs/{id}/subscription | Get org subscription
[**list_orgs**](OrgsApi.md#list_orgs) | **GET** /orgs | List orgs
[**preflight_app_service_capacity**](OrgsApi.md#preflight_app_service_capacity) | **POST** /orgs/{id}/actions/preflight-app-service-capacity | Preflight app-service capacity
[**update_org**](OrgsApi.md#update_org) | **PUT** /orgs/{id} | Update org


# **get_org**
> Org get_org(id)

Get org

Returns the org identified by the request path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.org import Org
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
    api_instance = wodby.OrgsApi(api_client)
    id = 56 # int | 

    try:
        # Get org
        api_response = api_instance.get_org(id)
        print("The response of OrgsApi->get_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->get_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Org**](Org.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Org |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_subscription**
> OrgSubscriptionDetails get_org_subscription(id)

Get org subscription

Returns usage and pricing details for callers with billing-view access to the organization.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.org_subscription_details import OrgSubscriptionDetails
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
    api_instance = wodby.OrgsApi(api_client)
    id = 56 # int | 

    try:
        # Get org subscription
        api_response = api_instance.get_org_subscription(id)
        print("The response of OrgsApi->get_org_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->get_org_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OrgSubscriptionDetails**](OrgSubscriptionDetails.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Organization subscription details |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orgs**
> List[Org] list_orgs()

List orgs

Returns orgs matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.org import Org
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
    api_instance = wodby.OrgsApi(api_client)

    try:
        # List orgs
        api_response = api_instance.list_orgs()
        print("The response of OrgsApi->list_orgs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->list_orgs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Org]**](Org.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of orgs |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preflight_app_service_capacity**
> AppServiceCapacityPreflight preflight_app_service_capacity(id, app_service_capacity_preflight_request)

Preflight app-service capacity

Evaluates whether the organization can add the requested number of enabled app services under the backend's effective billing policy.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_capacity_preflight import AppServiceCapacityPreflight
from wodby.models.app_service_capacity_preflight_request import AppServiceCapacityPreflightRequest
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
    api_instance = wodby.OrgsApi(api_client)
    id = 56 # int | 
    app_service_capacity_preflight_request = wodby.AppServiceCapacityPreflightRequest() # AppServiceCapacityPreflightRequest | 

    try:
        # Preflight app-service capacity
        api_response = api_instance.preflight_app_service_capacity(id, app_service_capacity_preflight_request)
        print("The response of OrgsApi->preflight_app_service_capacity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->preflight_app_service_capacity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_service_capacity_preflight_request** | [**AppServiceCapacityPreflightRequest**](AppServiceCapacityPreflightRequest.md)|  | 

### Return type

[**AppServiceCapacityPreflight**](AppServiceCapacityPreflight.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Effective app-service capacity decision |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_org**
> Org update_org(id, update_org_request)

Update org

Updates the org and returns the updated resource.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.org import Org
from wodby.models.update_org_request import UpdateOrgRequest
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
    api_instance = wodby.OrgsApi(api_client)
    id = 56 # int | 
    update_org_request = wodby.UpdateOrgRequest() # UpdateOrgRequest | 

    try:
        # Update org
        api_response = api_instance.update_org(id, update_org_request)
        print("The response of OrgsApi->update_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->update_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_org_request** | [**UpdateOrgRequest**](UpdateOrgRequest.md)|  | 

### Return type

[**Org**](Org.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated org |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

