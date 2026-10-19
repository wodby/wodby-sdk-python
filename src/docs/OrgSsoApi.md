# wodby.OrgSsoApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_org_sso_provider**](OrgSsoApi.md#create_org_sso_provider) | **POST** /org-sso-providers | Create organization SSO provider
[**delete_org_sso_provider**](OrgSsoApi.md#delete_org_sso_provider) | **DELETE** /org-sso-providers/{id} | Delete organization SSO provider
[**get_org_sso_provider**](OrgSsoApi.md#get_org_sso_provider) | **GET** /org-sso-providers/{id} | Get organization SSO provider
[**list_org_sso_providers**](OrgSsoApi.md#list_org_sso_providers) | **GET** /org-sso-providers | List organization SSO providers
[**update_org_sso_provider**](OrgSsoApi.md#update_org_sso_provider) | **PUT** /org-sso-providers/{id} | Update organization SSO provider
[**verify_org_sso_domain**](OrgSsoApi.md#verify_org_sso_domain) | **POST** /org-sso-providers/{id}/actions/verify-domain | Verify SSO domain


# **create_org_sso_provider**
> OrgSSOProvider create_org_sso_provider(org_sso_provider_input)

Create organization SSO provider

Adds an OIDC, GitHub or SAML single sign-on provider. The client secret is write-only.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.org_sso_provider import OrgSSOProvider
from wodby.models.org_sso_provider_input import OrgSSOProviderInput
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
    api_instance = wodby.OrgSsoApi(api_client)
    org_sso_provider_input = wodby.OrgSSOProviderInput() # OrgSSOProviderInput | 

    try:
        # Create organization SSO provider
        api_response = api_instance.create_org_sso_provider(org_sso_provider_input)
        print("The response of OrgSsoApi->create_org_sso_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSsoApi->create_org_sso_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_sso_provider_input** | [**OrgSSOProviderInput**](OrgSSOProviderInput.md)|  | 

### Return type

[**OrgSSOProvider**](OrgSSOProvider.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created SSO provider |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_org_sso_provider**
> OperationResult delete_org_sso_provider(id)

Delete organization SSO provider

Deletes a single sign-on provider.

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
    api_instance = wodby.OrgSsoApi(api_client)
    id = 56 # int | 

    try:
        # Delete organization SSO provider
        api_response = api_instance.delete_org_sso_provider(id)
        print("The response of OrgSsoApi->delete_org_sso_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSsoApi->delete_org_sso_provider: %s\n" % e)
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

# **get_org_sso_provider**
> OrgSSOProvider get_org_sso_provider(id)

Get organization SSO provider

Returns one single sign-on provider with its domains.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.org_sso_provider import OrgSSOProvider
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
    api_instance = wodby.OrgSsoApi(api_client)
    id = 56 # int | 

    try:
        # Get organization SSO provider
        api_response = api_instance.get_org_sso_provider(id)
        print("The response of OrgSsoApi->get_org_sso_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSsoApi->get_org_sso_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OrgSSOProvider**](OrgSSOProvider.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSO provider |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_org_sso_providers**
> List[OrgSSOProvider] list_org_sso_providers(org_id=org_id)

List organization SSO providers

Returns the single sign-on providers of the organization with their domains.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.org_sso_provider import OrgSSOProvider
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
    api_instance = wodby.OrgSsoApi(api_client)
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)

    try:
        # List organization SSO providers
        api_response = api_instance.list_org_sso_providers(org_id=org_id)
        print("The response of OrgSsoApi->list_org_sso_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSsoApi->list_org_sso_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 

### Return type

[**List[OrgSSOProvider]**](OrgSSOProvider.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSO providers |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_org_sso_provider**
> OrgSSOProvider update_org_sso_provider(id, org_sso_provider_input)

Update organization SSO provider

Replaces the provider settings. Leave clientSecret out to keep the stored secret.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.org_sso_provider import OrgSSOProvider
from wodby.models.org_sso_provider_input import OrgSSOProviderInput
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
    api_instance = wodby.OrgSsoApi(api_client)
    id = 56 # int | 
    org_sso_provider_input = wodby.OrgSSOProviderInput() # OrgSSOProviderInput | 

    try:
        # Update organization SSO provider
        api_response = api_instance.update_org_sso_provider(id, org_sso_provider_input)
        print("The response of OrgSsoApi->update_org_sso_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSsoApi->update_org_sso_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **org_sso_provider_input** | [**OrgSSOProviderInput**](OrgSSOProviderInput.md)|  | 

### Return type

[**OrgSSOProvider**](OrgSSOProvider.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated SSO provider |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_org_sso_domain**
> OrgSSODomain verify_org_sso_domain(id, verify_org_sso_domain_input)

Verify SSO domain

Checks the DNS TXT record that proves the organization owns one of the provider's email domains and returns the domain.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.org_sso_domain import OrgSSODomain
from wodby.models.verify_org_sso_domain_input import VerifyOrgSSODomainInput
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
    api_instance = wodby.OrgSsoApi(api_client)
    id = 56 # int | 
    verify_org_sso_domain_input = wodby.VerifyOrgSSODomainInput() # VerifyOrgSSODomainInput | 

    try:
        # Verify SSO domain
        api_response = api_instance.verify_org_sso_domain(id, verify_org_sso_domain_input)
        print("The response of OrgSsoApi->verify_org_sso_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSsoApi->verify_org_sso_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **verify_org_sso_domain_input** | [**VerifyOrgSSODomainInput**](VerifyOrgSSODomainInput.md)|  | 

### Return type

[**OrgSSODomain**](OrgSSODomain.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain with its verification state |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

