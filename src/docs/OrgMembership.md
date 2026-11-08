# OrgMembership


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**user_id** | **int** |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**email** | **str** |  | [optional] 
**org_id** | **int** |  | 
**role** | **str** |  | 
**status** | **str** |  | 
**joined_at** | **datetime** |  | [optional] 
**project_memberships** | [**List[ProjectMembership]**](ProjectMembership.md) | The member&#39;s project access: their direct project memberships, then the memberships of every team they belong to (those have teamId set). Returned for a single membership to organization owners, admins and support members; omitted otherwise. | [optional] 
**team_memberships** | [**List[OrgMembershipTeamMembership]**](OrgMembershipTeamMembership.md) | The teams the member belongs to. Returned for a single membership to organization owners, admins and support members; omitted otherwise. | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.org_membership import OrgMembership

# TODO update the JSON string below
json = "{}"
# create an instance of OrgMembership from a JSON string
org_membership_instance = OrgMembership.from_json(json)
# print the JSON string representation of the object
print(OrgMembership.to_json())

# convert the object into a dict
org_membership_dict = org_membership_instance.to_dict()
# create an instance of OrgMembership from a dict
org_membership_from_dict = OrgMembership.from_dict(org_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


