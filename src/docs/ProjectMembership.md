# ProjectMembership


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**project_id** | **int** |  | 
**org_membership_id** | **int** |  | [optional] 
**team_id** | **int** |  | [optional] 
**role** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.project_membership import ProjectMembership

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMembership from a JSON string
project_membership_instance = ProjectMembership.from_json(json)
# print the JSON string representation of the object
print(ProjectMembership.to_json())

# convert the object into a dict
project_membership_dict = project_membership_instance.to_dict()
# create an instance of ProjectMembership from a dict
project_membership_from_dict = ProjectMembership.from_dict(project_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


