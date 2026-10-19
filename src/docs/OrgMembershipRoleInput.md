# OrgMembershipRoleInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 

## Example

```python
from wodby.models.org_membership_role_input import OrgMembershipRoleInput

# TODO update the JSON string below
json = "{}"
# create an instance of OrgMembershipRoleInput from a JSON string
org_membership_role_input_instance = OrgMembershipRoleInput.from_json(json)
# print the JSON string representation of the object
print(OrgMembershipRoleInput.to_json())

# convert the object into a dict
org_membership_role_input_dict = org_membership_role_input_instance.to_dict()
# create an instance of OrgMembershipRoleInput from a dict
org_membership_role_input_from_dict = OrgMembershipRoleInput.from_dict(org_membership_role_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


