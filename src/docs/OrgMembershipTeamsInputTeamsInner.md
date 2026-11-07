# OrgMembershipTeamsInputTeamsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **int** |  | 
**role** | **str** |  | 

## Example

```python
from wodby.models.org_membership_teams_input_teams_inner import OrgMembershipTeamsInputTeamsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrgMembershipTeamsInputTeamsInner from a JSON string
org_membership_teams_input_teams_inner_instance = OrgMembershipTeamsInputTeamsInner.from_json(json)
# print the JSON string representation of the object
print(OrgMembershipTeamsInputTeamsInner.to_json())

# convert the object into a dict
org_membership_teams_input_teams_inner_dict = org_membership_teams_input_teams_inner_instance.to_dict()
# create an instance of OrgMembershipTeamsInputTeamsInner from a dict
org_membership_teams_input_teams_inner_from_dict = OrgMembershipTeamsInputTeamsInner.from_dict(org_membership_teams_input_teams_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


