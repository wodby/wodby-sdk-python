# OrgSSODomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**domain** | **str** |  | 
**verified** | **bool** |  | 
**verification_record_name** | **str** | DNS record name to create for verification. | 
**verification_record_type** | **str** |  | 
**verification_record_value** | **str** |  | 
**verified_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.org_sso_domain import OrgSSODomain

# TODO update the JSON string below
json = "{}"
# create an instance of OrgSSODomain from a JSON string
org_sso_domain_instance = OrgSSODomain.from_json(json)
# print the JSON string representation of the object
print(OrgSSODomain.to_json())

# convert the object into a dict
org_sso_domain_dict = org_sso_domain_instance.to_dict()
# create an instance of OrgSSODomain from a dict
org_sso_domain_from_dict = OrgSSODomain.from_dict(org_sso_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


