# wodby.ProjectRolesApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_role**](ProjectRolesApi.md#create_project_role) | **POST** /project-roles | Create custom project role
[**delete_project_role**](ProjectRolesApi.md#delete_project_role) | **DELETE** /project-roles/{id} | Delete custom project role
[**get_project_role**](ProjectRolesApi.md#get_project_role) | **GET** /project-roles/{id} | Get custom project role
[**list_project_permissions**](ProjectRolesApi.md#list_project_permissions) | **GET** /project-permissions | List project permissions
[**list_project_roles**](ProjectRolesApi.md#list_project_roles) | **GET** /project-roles | List project roles
[**update_project_role**](ProjectRolesApi.md#update_project_role) | **PUT** /project-roles/{id} | Update custom project role


# **create_project_role**
> ProjectRole create_project_role(project_role_input)

Create custom project role

Adds a custom project role to the organization. Organization owners and admins only. project.view is always granted, and env.view and env.logs are granted in every environment type, because every project member can see the project's environments and read their logs.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.project_role import ProjectRole
from wodby.models.project_role_input import ProjectRoleInput
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
    api_instance = wodby.ProjectRolesApi(api_client)
    project_role_input = wodby.ProjectRoleInput() # ProjectRoleInput | 

    try:
        # Create custom project role
        api_response = api_instance.create_project_role(project_role_input)
        print("The response of ProjectRolesApi->create_project_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectRolesApi->create_project_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_role_input** | [**ProjectRoleInput**](ProjectRoleInput.md)|  | 

### Return type

[**ProjectRole**](ProjectRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created role |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_role**
> OperationResult delete_project_role(id)

Delete custom project role

Deletes a custom project role that no project membership holds. Organization owners and admins only.

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
    api_instance = wodby.ProjectRolesApi(api_client)
    id = 56 # int | 

    try:
        # Delete custom project role
        api_response = api_instance.delete_project_role(id)
        print("The response of ProjectRolesApi->delete_project_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectRolesApi->delete_project_role: %s\n" % e)
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
**200** | Deletion result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_role**
> ProjectRole get_project_role(id)

Get custom project role

Returns a custom project role.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.project_role import ProjectRole
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
    api_instance = wodby.ProjectRolesApi(api_client)
    id = 56 # int | 

    try:
        # Get custom project role
        api_response = api_instance.get_project_role(id)
        print("The response of ProjectRolesApi->get_project_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectRolesApi->get_project_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ProjectRole**](ProjectRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom role |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_permissions**
> List[ProjectPermission] list_project_permissions()

List project permissions

Returns every permission a project role can grant, in display order.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.project_permission import ProjectPermission
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
    api_instance = wodby.ProjectRolesApi(api_client)

    try:
        # List project permissions
        api_response = api_instance.list_project_permissions()
        print("The response of ProjectRolesApi->list_project_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectRolesApi->list_project_permissions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ProjectPermission]**](ProjectPermission.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project permissions |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_roles**
> List[ProjectRole] list_project_roles(org_id=org_id)

List project roles

Returns the system project roles from least to most access, then the organization's custom roles by title, with the permissions each grants.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.project_role import ProjectRole
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
    api_instance = wodby.ProjectRolesApi(api_client)
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)

    try:
        # List project roles
        api_response = api_instance.list_project_roles(org_id=org_id)
        print("The response of ProjectRolesApi->list_project_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectRolesApi->list_project_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 

### Return type

[**List[ProjectRole]**](ProjectRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project roles |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_role**
> ProjectRole update_project_role(id, project_role_input)

Update custom project role

Replaces a custom role's name, title, description and permissions. Every membership holding the role changes at once. A role that teams hold cannot get project.manage. Organization owners and admins only.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.project_role import ProjectRole
from wodby.models.project_role_input import ProjectRoleInput
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
    api_instance = wodby.ProjectRolesApi(api_client)
    id = 56 # int | 
    project_role_input = wodby.ProjectRoleInput() # ProjectRoleInput | 

    try:
        # Update custom project role
        api_response = api_instance.update_project_role(id, project_role_input)
        print("The response of ProjectRolesApi->update_project_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectRolesApi->update_project_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **project_role_input** | [**ProjectRoleInput**](ProjectRoleInput.md)|  | 

### Return type

[**ProjectRole**](ProjectRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated role |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

