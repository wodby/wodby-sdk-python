# OrgSSOProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**org_id** | **int** |  | 
**name** | **str** |  | 
**kind** | **str** | Provider kind, such as oidc, github or saml. | 
**issuer_url** | **str** |  | 
**client_id** | **str** |  | 
**github_org** | **str** |  | [optional] 
**saml_idp_metadata_url** | **str** |  | [optional] 
**saml_sp_entity_id** | **str** | Entity ID to configure in the SAML identity provider. | [optional] 
**saml_sp_metadata_url** | **str** |  | [optional] 
**saml_acs_url** | **str** | Assertion consumer service URL to configure in the SAML identity provider. | [optional] 
**enabled** | **bool** |  | 
**jit_enabled** | **bool** | Create a membership on first sign-in for people from a verified domain. | 
**domains** | [**List[OrgSSODomain]**](OrgSSODomain.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.org_sso_provider import OrgSSOProvider

# TODO update the JSON string below
json = "{}"
# create an instance of OrgSSOProvider from a JSON string
org_sso_provider_instance = OrgSSOProvider.from_json(json)
# print the JSON string representation of the object
print(OrgSSOProvider.to_json())

# convert the object into a dict
org_sso_provider_dict = org_sso_provider_instance.to_dict()
# create an instance of OrgSSOProvider from a dict
org_sso_provider_from_dict = OrgSSOProvider.from_dict(org_sso_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


