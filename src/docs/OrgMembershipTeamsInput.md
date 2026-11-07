# OrgMembershipTeamsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | [**List[OrgMembershipTeamsInputTeamsInner]**](OrgMembershipTeamsInputTeamsInner.md) | The complete team list of the member. | 

## Example

```python
from wodby.models.org_membership_teams_input import OrgMembershipTeamsInput

# TODO update the JSON string below
json = "{}"
# create an instance of OrgMembershipTeamsInput from a JSON string
org_membership_teams_input_instance = OrgMembershipTeamsInput.from_json(json)
# print the JSON string representation of the object
print(OrgMembershipTeamsInput.to_json())

# convert the object into a dict
org_membership_teams_input_dict = org_membership_teams_input_instance.to_dict()
# create an instance of OrgMembershipTeamsInput from a dict
org_membership_teams_input_from_dict = OrgMembershipTeamsInput.from_dict(org_membership_teams_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


