# NewProjectMembershipsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**org_membership_ids** | **List[int]** |  | [optional] 
**team_ids** | **List[int]** |  | [optional] 
**role** | **str** |  | 

## Example

```python
from wodby.models.new_project_memberships_input import NewProjectMembershipsInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewProjectMembershipsInput from a JSON string
new_project_memberships_input_instance = NewProjectMembershipsInput.from_json(json)
# print the JSON string representation of the object
print(NewProjectMembershipsInput.to_json())

# convert the object into a dict
new_project_memberships_input_dict = new_project_memberships_input_instance.to_dict()
# create an instance of NewProjectMembershipsInput from a dict
new_project_memberships_input_from_dict = NewProjectMembershipsInput.from_dict(new_project_memberships_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


