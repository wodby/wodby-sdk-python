# wodby.AppInstancesApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app_access**](AppInstancesApi.md#create_app_access) | **POST** /app-instance-accesses/{id} | Create app instance access
[**create_app_instance**](AppInstancesApi.md#create_app_instance) | **POST** /app-instances | Create app instance
[**delete_app_access**](AppInstancesApi.md#delete_app_access) | **DELETE** /app-accesses/{id} | Delete app access
[**delete_app_instance**](AppInstancesApi.md#delete_app_instance) | **DELETE** /app-instances/{id} | Delete app instance
[**get_app_instance**](AppInstancesApi.md#get_app_instance) | **GET** /app-instances/{id} | Get app instance
[**get_app_instance_access**](AppInstancesApi.md#get_app_instance_access) | **GET** /app-instance-accesses/{id} | Get app instance access
[**get_app_instance_by_name**](AppInstancesApi.md#get_app_instance_by_name) | **GET** /app-instances/by-name/{appName}/{instanceName} | Get app instance by app and instance name
[**get_app_instance_cicd_settings**](AppInstancesApi.md#get_app_instance_cicd_settings) | **GET** /app-instances/cicd-settings/{id} | Get app instance CI/CD settings
[**get_app_instance_stack_upgrade_changelog**](AppInstancesApi.md#get_app_instance_stack_upgrade_changelog) | **GET** /app-instance-stack-upgrade-changelogs/{id} | Preview app instance stack upgrade
[**list_app_access_cleanups**](AppInstancesApi.md#list_app_access_cleanups) | **GET** /app-access-cleanups | List app-access cleanups
[**list_app_instances**](AppInstancesApi.md#list_app_instances) | **GET** /app-instances | List app instances
[**preflight_app_access**](AppInstancesApi.md#preflight_app_access) | **POST** /app-accesses/actions/preflight | Preflight app instance access
[**retry_app_access_cleanup**](AppInstancesApi.md#retry_app_access_cleanup) | **POST** /app-access-cleanups/{id}/actions/retry | Retry app-access cleanup
[**update_app_access**](AppInstancesApi.md#update_app_access) | **PUT** /app-accesses/{id} | Update app access
[**update_app_instance**](AppInstancesApi.md#update_app_instance) | **PUT** /app-instances/{id} | Update app instance
[**update_app_instance_cicd_settings**](AppInstancesApi.md#update_app_instance_cicd_settings) | **PUT** /app-instances/cicd-settings/{id} | Update app instance CI/CD settings
[**update_app_instance_maintenance_mode**](AppInstancesApi.md#update_app_instance_maintenance_mode) | **PUT** /app-instances/{id}/actions/maintenance-mode | Update app instance maintenance mode
[**update_app_instance_settings**](AppInstancesApi.md#update_app_instance_settings) | **PUT** /app-instances/settings/{id} | Update app instance settings
[**upgrade_app_instance_stack**](AppInstancesApi.md#upgrade_app_instance_stack) | **POST** /app-instances/{id}/actions/upgrade-stack | Upgrade app instance stack


# **create_app_access**
> AppAccessOperationResult create_app_access(id, new_app_access_input)

Create app instance access

Creates external access for the app instance identified by the path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_access_operation_result import AppAccessOperationResult
from wodby.models.new_app_access_input import NewAppAccessInput
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
    api_instance = wodby.AppInstancesApi(api_client)
    id = 56 # int | 
    new_app_access_input = wodby.NewAppAccessInput() # NewAppAccessInput | 

    try:
        # Create app instance access
        api_response = api_instance.create_app_access(id, new_app_access_input)
        print("The response of AppInstancesApi->create_app_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->create_app_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **new_app_access_input** | [**NewAppAccessInput**](NewAppAccessInput.md)|  | 

### Return type

[**AppAccessOperationResult**](AppAccessOperationResult.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created app access and provisioning task |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app_instance**
> AppInstance create_app_instance(new_app_instance_input)

Create app instance

Creates an app instance and returns the created resource.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_instance import AppInstance
from wodby.models.new_app_instance_input import NewAppInstanceInput
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
    api_instance = wodby.AppInstancesApi(api_client)
    new_app_instance_input = wodby.NewAppInstanceInput() # NewAppInstanceInput | 

    try:
        # Create app instance
        api_response = api_instance.create_app_instance(new_app_instance_input)
        print("The response of AppInstancesApi->create_app_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->create_app_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_app_instance_input** | [**NewAppInstanceInput**](NewAppInstanceInput.md)|  | 

### Return type

[**AppInstance**](AppInstance.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created app instance |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_access**
> OperationResult delete_app_access(id)

Delete app access

Removes app access and returns the cleanup task identifier.

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
    api_instance = wodby.AppInstancesApi(api_client)
    id = 56 # int | 

    try:
        # Delete app access
        api_response = api_instance.delete_app_access(id)
        print("The response of AppInstancesApi->delete_app_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->delete_app_access: %s\n" % e)
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
**200** | Delete operation result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_instance**
> OperationResult delete_app_instance(id, force=force)

Delete app instance

Deletes the app instance and returns the operation result.

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
    api_instance = wodby.AppInstancesApi(api_client)
    id = 56 # int | 
    force = False # bool |  (optional) (default to False)

    try:
        # Delete app instance
        api_response = api_instance.delete_app_instance(id, force=force)
        print("The response of AppInstancesApi->delete_app_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->delete_app_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **force** | **bool**|  | [optional] [default to False]

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

# **get_app_instance**
> AppInstance get_app_instance(id)

Get app instance

Returns the app instance identified by the request path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_instance import AppInstance
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
    api_instance = wodby.AppInstancesApi(api_client)
    id = 56 # int | 

    try:
        # Get app instance
        api_response = api_instance.get_app_instance(id)
        print("The response of AppInstancesApi->get_app_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->get_app_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AppInstance**](AppInstance.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App instance |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_instance_access**
> AppAccess get_app_instance_access(id)

Get app instance access

Returns the external access configuration for the app instance identified by the path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_access import AppAccess
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
    api_instance = wodby.AppInstancesApi(api_client)
    id = 56 # int | 

    try:
        # Get app instance access
        api_response = api_instance.get_app_instance_access(id)
        print("The response of AppInstancesApi->get_app_instance_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->get_app_instance_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AppAccess**](AppAccess.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App access configuration |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_instance_by_name**
> AppInstance get_app_instance_by_name(app_name, instance_name, org_id=org_id)

Get app instance by app and instance name

Returns the app instance identified by app and instance name.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_instance import AppInstance
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
    api_instance = wodby.AppInstancesApi(api_client)
    app_name = 'app_name_example' # str | 
    instance_name = 'instance_name_example' # str | 
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)

    try:
        # Get app instance by app and instance name
        api_response = api_instance.get_app_instance_by_name(app_name, instance_name, org_id=org_id)
        print("The response of AppInstancesApi->get_app_instance_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->get_app_instance_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**|  | 
 **instance_name** | **str**|  | 
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 

### Return type

[**AppInstance**](AppInstance.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App instance |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_instance_cicd_settings**
> AppInstanceCICDSettings get_app_instance_cicd_settings(id)

Get app instance CI/CD settings

Returns the CI and registry integrations used by future app instance builds. Integration ID 0 identifies the built-in Wodby service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_instance_cicd_settings import AppInstanceCICDSettings
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
    api_instance = wodby.AppInstancesApi(api_client)
    id = 56 # int | 

    try:
        # Get app instance CI/CD settings
        api_response = api_instance.get_app_instance_cicd_settings(id)
        print("The response of AppInstancesApi->get_app_instance_cicd_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->get_app_instance_cicd_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AppInstanceCICDSettings**](AppInstanceCICDSettings.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App instance CI/CD settings |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_instance_stack_upgrade_changelog**
> AppInstanceStackUpgradeChangelog get_app_instance_stack_upgrade_changelog(id)

Preview app instance stack upgrade

Returns the stack and service revision changes that an app instance stack upgrade would apply.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_instance_stack_upgrade_changelog import AppInstanceStackUpgradeChangelog
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
    api_instance = wodby.AppInstancesApi(api_client)
    id = 56 # int | 

    try:
        # Preview app instance stack upgrade
        api_response = api_instance.get_app_instance_stack_upgrade_changelog(id)
        print("The response of AppInstancesApi->get_app_instance_stack_upgrade_changelog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->get_app_instance_stack_upgrade_changelog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AppInstanceStackUpgradeChangelog**](AppInstanceStackUpgradeChangelog.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stack upgrade changelog |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_access_cleanups**
> List[AppAccessCleanup] list_app_access_cleanups(app_instance_id=app_instance_id, integration_id=integration_id)

List app-access cleanups

Returns cleanup records for exactly one app instance or integration.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_access_cleanup import AppAccessCleanup
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
    api_instance = wodby.AppInstancesApi(api_client)
    app_instance_id = 56 # int |  (optional)
    integration_id = 56 # int |  (optional)

    try:
        # List app-access cleanups
        api_response = api_instance.list_app_access_cleanups(app_instance_id=app_instance_id, integration_id=integration_id)
        print("The response of AppInstancesApi->list_app_access_cleanups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->list_app_access_cleanups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_instance_id** | **int**|  | [optional] 
 **integration_id** | **int**|  | [optional] 

### Return type

[**List[AppAccessCleanup]**](AppAccessCleanup.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cleanup records |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_instances**
> List[AppInstance] list_app_instances(org_id=org_id, project_ids=project_ids, app_id=app_id, cluster_id=cluster_id, cluster_app=cluster_app)

List app instances

Returns app instances matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_instance import AppInstance
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
    api_instance = wodby.AppInstancesApi(api_client)
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)
    project_ids = 'project_ids_example' # str | Comma-separated project ids (optional)
    app_id = 56 # int |  (optional)
    cluster_id = 56 # int |  (optional)
    cluster_app = True # bool |  (optional)

    try:
        # List app instances
        api_response = api_instance.list_app_instances(org_id=org_id, project_ids=project_ids, app_id=app_id, cluster_id=cluster_id, cluster_app=cluster_app)
        print("The response of AppInstancesApi->list_app_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->list_app_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 
 **project_ids** | **str**| Comma-separated project ids | [optional] 
 **app_id** | **int**|  | [optional] 
 **cluster_id** | **int**|  | [optional] 
 **cluster_app** | **bool**|  | [optional] 

### Return type

[**List[AppInstance]**](AppInstance.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of app instances |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preflight_app_access**
> ValidationResult preflight_app_access(new_app_instance_access_input)

Preflight app instance access

Validates a proposed app-access configuration before an app instance or access resource is created.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.new_app_instance_access_input import NewAppInstanceAccessInput
from wodby.models.validation_result import ValidationResult
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
    api_instance = wodby.AppInstancesApi(api_client)
    new_app_instance_access_input = wodby.NewAppInstanceAccessInput() # NewAppInstanceAccessInput | 

    try:
        # Preflight app instance access
        api_response = api_instance.preflight_app_access(new_app_instance_access_input)
        print("The response of AppInstancesApi->preflight_app_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->preflight_app_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_app_instance_access_input** | [**NewAppInstanceAccessInput**](NewAppInstanceAccessInput.md)|  | 

### Return type

[**ValidationResult**](ValidationResult.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Preflight result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_app_access_cleanup**
> OperationResult retry_app_access_cleanup(id)

Retry app-access cleanup

Retries a failed app-access cleanup and returns its task identifier.

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
    api_instance = wodby.AppInstancesApi(api_client)
    id = 56 # int | 

    try:
        # Retry app-access cleanup
        api_response = api_instance.retry_app_access_cleanup(id)
        print("The response of AppInstancesApi->retry_app_access_cleanup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->retry_app_access_cleanup: %s\n" % e)
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
**200** | Retry operation result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_access**
> AppAccessOperationResult update_app_access(id, update_app_access_input)

Update app access

Updates an existing app-access configuration and starts its reconciliation task.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_access_operation_result import AppAccessOperationResult
from wodby.models.update_app_access_input import UpdateAppAccessInput
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
    api_instance = wodby.AppInstancesApi(api_client)
    id = 56 # int | 
    update_app_access_input = wodby.UpdateAppAccessInput() # UpdateAppAccessInput | 

    try:
        # Update app access
        api_response = api_instance.update_app_access(id, update_app_access_input)
        print("The response of AppInstancesApi->update_app_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->update_app_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_app_access_input** | [**UpdateAppAccessInput**](UpdateAppAccessInput.md)|  | 

### Return type

[**AppAccessOperationResult**](AppAccessOperationResult.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated app access and reconciliation task |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_instance**
> AppInstance update_app_instance(id, update_title_request)

Update app instance

Updates the app instance and returns the updated resource.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_instance import AppInstance
from wodby.models.update_title_request import UpdateTitleRequest
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
    api_instance = wodby.AppInstancesApi(api_client)
    id = 56 # int | 
    update_title_request = wodby.UpdateTitleRequest() # UpdateTitleRequest | 

    try:
        # Update app instance
        api_response = api_instance.update_app_instance(id, update_title_request)
        print("The response of AppInstancesApi->update_app_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->update_app_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_title_request** | [**UpdateTitleRequest**](UpdateTitleRequest.md)|  | 

### Return type

[**AppInstance**](AppInstance.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated app instance |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_instance_cicd_settings**
> AppInstanceCICDSettings update_app_instance_cicd_settings(id, app_instance_cicd_settings_input)

Update app instance CI/CD settings

Updates the CI and registry integrations used by future app instance builds. Integration ID 0 selects the built-in Wodby service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_instance_cicd_settings import AppInstanceCICDSettings
from wodby.models.app_instance_cicd_settings_input import AppInstanceCICDSettingsInput
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
    api_instance = wodby.AppInstancesApi(api_client)
    id = 56 # int | 
    app_instance_cicd_settings_input = wodby.AppInstanceCICDSettingsInput() # AppInstanceCICDSettingsInput | 

    try:
        # Update app instance CI/CD settings
        api_response = api_instance.update_app_instance_cicd_settings(id, app_instance_cicd_settings_input)
        print("The response of AppInstancesApi->update_app_instance_cicd_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->update_app_instance_cicd_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_instance_cicd_settings_input** | [**AppInstanceCICDSettingsInput**](AppInstanceCICDSettingsInput.md)|  | 

### Return type

[**AppInstanceCICDSettings**](AppInstanceCICDSettings.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated app instance CI/CD settings |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_instance_maintenance_mode**
> OperationResult update_app_instance_maintenance_mode(id, app_instance_maintenance_mode_input)

Update app instance maintenance mode

Enables or disables the fixed maintenance response on all public HTTP routes while application workloads continue running.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_instance_maintenance_mode_input import AppInstanceMaintenanceModeInput
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
    api_instance = wodby.AppInstancesApi(api_client)
    id = 56 # int | 
    app_instance_maintenance_mode_input = wodby.AppInstanceMaintenanceModeInput() # AppInstanceMaintenanceModeInput | 

    try:
        # Update app instance maintenance mode
        api_response = api_instance.update_app_instance_maintenance_mode(id, app_instance_maintenance_mode_input)
        print("The response of AppInstancesApi->update_app_instance_maintenance_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->update_app_instance_maintenance_mode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_instance_maintenance_mode_input** | [**AppInstanceMaintenanceModeInput**](AppInstanceMaintenanceModeInput.md)|  | 

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
**200** | Maintenance mode update result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_instance_settings**
> AppInstance update_app_instance_settings(id, app_instance_settings_input)

Update app instance settings

Updates app instance settings and returns the updated app instance.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_instance import AppInstance
from wodby.models.app_instance_settings_input import AppInstanceSettingsInput
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
    api_instance = wodby.AppInstancesApi(api_client)
    id = 56 # int | 
    app_instance_settings_input = wodby.AppInstanceSettingsInput() # AppInstanceSettingsInput | 

    try:
        # Update app instance settings
        api_response = api_instance.update_app_instance_settings(id, app_instance_settings_input)
        print("The response of AppInstancesApi->update_app_instance_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->update_app_instance_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_instance_settings_input** | [**AppInstanceSettingsInput**](AppInstanceSettingsInput.md)|  | 

### Return type

[**AppInstance**](AppInstance.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated app instance |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_app_instance_stack**
> OperationResult upgrade_app_instance_stack(id, app_instance_stack_upgrade_input)

Upgrade app instance stack

Upgrades an app instance stack using the selected upgrade sections.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_instance_stack_upgrade_input import AppInstanceStackUpgradeInput
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
    api_instance = wodby.AppInstancesApi(api_client)
    id = 56 # int | 
    app_instance_stack_upgrade_input = wodby.AppInstanceStackUpgradeInput() # AppInstanceStackUpgradeInput | 

    try:
        # Upgrade app instance stack
        api_response = api_instance.upgrade_app_instance_stack(id, app_instance_stack_upgrade_input)
        print("The response of AppInstancesApi->upgrade_app_instance_stack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->upgrade_app_instance_stack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_instance_stack_upgrade_input** | [**AppInstanceStackUpgradeInput**](AppInstanceStackUpgradeInput.md)|  | 

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
**200** | Upgrade result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

