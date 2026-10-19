# wodby.OrgMembershipsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_org_membership**](OrgMembershipsApi.md#delete_org_membership) | **DELETE** /org-memberships/{id} | Remove organization member
[**get_org_membership**](OrgMembershipsApi.md#get_org_membership) | **GET** /org-memberships/{id} | Get org membership
[**invite_org_member**](OrgMembershipsApi.md#invite_org_member) | **POST** /org-memberships | Invite organization member
[**list_org_memberships**](OrgMembershipsApi.md#list_org_memberships) | **GET** /org-memberships | List org memberships
[**update_org_membership**](OrgMembershipsApi.md#update_org_membership) | **PUT** /org-memberships/{id} | Update organization member role


# **delete_org_membership**
> OperationResult delete_org_membership(id)

Remove organization member

Removes a member or a pending invitation from the organization.

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
    api_instance = wodby.OrgMembershipsApi(api_client)
    id = 56 # int | 

    try:
        # Remove organization member
        api_response = api_instance.delete_org_membership(id)
        print("The response of OrgMembershipsApi->delete_org_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgMembershipsApi->delete_org_membership: %s\n" % e)
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

# **get_org_membership**
> OrgMembership get_org_membership(id)

Get org membership

Returns the org membership identified by the request path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.org_membership import OrgMembership
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
    api_instance = wodby.OrgMembershipsApi(api_client)
    id = 56 # int | 

    try:
        # Get org membership
        api_response = api_instance.get_org_membership(id)
        print("The response of OrgMembershipsApi->get_org_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgMembershipsApi->get_org_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OrgMembership**](OrgMembership.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Org membership |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_org_member**
> OrgMembership invite_org_member(invite_org_member_input)

Invite organization member

Invites a person by email with an organization role, optionally adding them to teams and projects. The membership has the invited status until they accept.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.invite_org_member_input import InviteOrgMemberInput
from wodby.models.org_membership import OrgMembership
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
    api_instance = wodby.OrgMembershipsApi(api_client)
    invite_org_member_input = wodby.InviteOrgMemberInput() # InviteOrgMemberInput | 

    try:
        # Invite organization member
        api_response = api_instance.invite_org_member(invite_org_member_input)
        print("The response of OrgMembershipsApi->invite_org_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgMembershipsApi->invite_org_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_org_member_input** | [**InviteOrgMemberInput**](InviteOrgMemberInput.md)|  | 

### Return type

[**OrgMembership**](OrgMembership.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Invited membership |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_org_memberships**
> List[OrgMembership] list_org_memberships(org_id=org_id)

List org memberships

Returns org memberships matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.org_membership import OrgMembership
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
    api_instance = wodby.OrgMembershipsApi(api_client)
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)

    try:
        # List org memberships
        api_response = api_instance.list_org_memberships(org_id=org_id)
        print("The response of OrgMembershipsApi->list_org_memberships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgMembershipsApi->list_org_memberships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 

### Return type

[**List[OrgMembership]**](OrgMembership.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of org memberships |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_org_membership**
> OrgMembership update_org_membership(id, org_membership_role_input)

Update organization member role

Changes the organization role of a member and returns the membership.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.org_membership import OrgMembership
from wodby.models.org_membership_role_input import OrgMembershipRoleInput
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
    api_instance = wodby.OrgMembershipsApi(api_client)
    id = 56 # int | 
    org_membership_role_input = wodby.OrgMembershipRoleInput() # OrgMembershipRoleInput | 

    try:
        # Update organization member role
        api_response = api_instance.update_org_membership(id, org_membership_role_input)
        print("The response of OrgMembershipsApi->update_org_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgMembershipsApi->update_org_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **org_membership_role_input** | [**OrgMembershipRoleInput**](OrgMembershipRoleInput.md)|  | 

### Return type

[**OrgMembership**](OrgMembership.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated membership |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

