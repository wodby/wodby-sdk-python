# wodby.ProjectMembershipsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_memberships**](ProjectMembershipsApi.md#create_project_memberships) | **POST** /project-memberships | Add project members
[**delete_project_membership**](ProjectMembershipsApi.md#delete_project_membership) | **DELETE** /project-memberships/{id} | Remove project membership
[**list_project_memberships**](ProjectMembershipsApi.md#list_project_memberships) | **GET** /project-memberships | List project memberships
[**update_project_membership**](ProjectMembershipsApi.md#update_project_membership) | **PUT** /project-memberships/{id} | Update project membership


# **create_project_memberships**
> List[ProjectMembership] create_project_memberships(new_project_memberships_input)

Add project members

Gives organization members or teams the same role in a project. Returns the created memberships.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.new_project_memberships_input import NewProjectMembershipsInput
from wodby.models.project_membership import ProjectMembership
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
    api_instance = wodby.ProjectMembershipsApi(api_client)
    new_project_memberships_input = wodby.NewProjectMembershipsInput() # NewProjectMembershipsInput | 

    try:
        # Add project members
        api_response = api_instance.create_project_memberships(new_project_memberships_input)
        print("The response of ProjectMembershipsApi->create_project_memberships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectMembershipsApi->create_project_memberships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_project_memberships_input** | [**NewProjectMembershipsInput**](NewProjectMembershipsInput.md)|  | 

### Return type

[**List[ProjectMembership]**](ProjectMembership.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created project memberships |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_membership**
> OperationResult delete_project_membership(id)

Remove project membership

Removes a member or team from a project.

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
    api_instance = wodby.ProjectMembershipsApi(api_client)
    id = 56 # int | 

    try:
        # Remove project membership
        api_response = api_instance.delete_project_membership(id)
        print("The response of ProjectMembershipsApi->delete_project_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectMembershipsApi->delete_project_membership: %s\n" % e)
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
**200** | Removal result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_memberships**
> List[ProjectMembership] list_project_memberships(project_id)

List project memberships

Returns the members and teams with a role in a project.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.project_membership import ProjectMembership
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
    api_instance = wodby.ProjectMembershipsApi(api_client)
    project_id = 56 # int | 

    try:
        # List project memberships
        api_response = api_instance.list_project_memberships(project_id)
        print("The response of ProjectMembershipsApi->list_project_memberships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectMembershipsApi->list_project_memberships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**List[ProjectMembership]**](ProjectMembership.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project memberships |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_membership**
> ProjectMembership update_project_membership(id, project_membership_role_input)

Update project membership

Changes the project role of a member or team.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.project_membership import ProjectMembership
from wodby.models.project_membership_role_input import ProjectMembershipRoleInput
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
    api_instance = wodby.ProjectMembershipsApi(api_client)
    id = 56 # int | 
    project_membership_role_input = wodby.ProjectMembershipRoleInput() # ProjectMembershipRoleInput | 

    try:
        # Update project membership
        api_response = api_instance.update_project_membership(id, project_membership_role_input)
        print("The response of ProjectMembershipsApi->update_project_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectMembershipsApi->update_project_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **project_membership_role_input** | [**ProjectMembershipRoleInput**](ProjectMembershipRoleInput.md)|  | 

### Return type

[**ProjectMembership**](ProjectMembership.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated project membership |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

