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


