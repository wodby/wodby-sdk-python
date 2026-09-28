# Workspace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_user_id** | **int** |  | 
**source_app_service_id** | **int** |  | 
**runner_state** | **str** |  | 
**preparation_state** | **str** |  | 
**access_error** | **str** |  | 
**base_ref** | **str** |  | 
**branch** | **str** |  | 
**initial_commit** | **str** |  | 
**initialized** | **bool** |  | 
**error** | **str** |  | 
**task_id** | **int** |  | 

## Example

```python
from wodby.models.workspace import Workspace

# TODO update the JSON string below
json = "{}"
# create an instance of Workspace from a JSON string
workspace_instance = Workspace.from_json(json)
# print the JSON string representation of the object
print(Workspace.to_json())

# convert the object into a dict
workspace_dict = workspace_instance.to_dict()
# create an instance of Workspace from a dict
workspace_from_dict = Workspace.from_dict(workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


