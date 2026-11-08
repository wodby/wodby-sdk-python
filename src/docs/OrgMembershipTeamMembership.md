# OrgMembershipTeamMembership


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**team_id** | **int** |  | 
**role** | **str** |  | 

## Example

```python
from wodby.models.org_membership_team_membership import OrgMembershipTeamMembership

# TODO update the JSON string below
json = "{}"
# create an instance of OrgMembershipTeamMembership from a JSON string
org_membership_team_membership_instance = OrgMembershipTeamMembership.from_json(json)
# print the JSON string representation of the object
print(OrgMembershipTeamMembership.to_json())

# convert the object into a dict
org_membership_team_membership_dict = org_membership_team_membership_instance.to_dict()
# create an instance of OrgMembershipTeamMembership from a dict
org_membership_team_membership_from_dict = OrgMembershipTeamMembership.from_dict(org_membership_team_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


