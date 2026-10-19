# OrgSSOProviderInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** | Used when creating a provider. Optional for API-key requests; defaults to the API key&#39;s organization. | [optional] 
**kind** | **str** | Provider kind when creating, such as oidc, github or saml. It cannot be changed. | [optional] 
**name** | **str** |  | 
**issuer_url** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** | OIDC or GitHub client secret. Leave it out on update to keep the stored secret. | [optional] 
**github_org** | **str** |  | [optional] 
**saml_idp_metadata_url** | **str** |  | [optional] 
**saml_idp_metadata_xml** | **str** |  | [optional] 
**enabled** | **bool** |  | 
**jit_enabled** | **bool** |  | 
**domains** | **List[str]** |  | 

## Example

```python
from wodby.models.org_sso_provider_input import OrgSSOProviderInput

# TODO update the JSON string below
json = "{}"
# create an instance of OrgSSOProviderInput from a JSON string
org_sso_provider_input_instance = OrgSSOProviderInput.from_json(json)
# print the JSON string representation of the object
print(OrgSSOProviderInput.to_json())

# convert the object into a dict
org_sso_provider_input_dict = org_sso_provider_input_instance.to_dict()
# create an instance of OrgSSOProviderInput from a dict
org_sso_provider_input_from_dict = OrgSSOProviderInput.from_dict(org_sso_provider_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


