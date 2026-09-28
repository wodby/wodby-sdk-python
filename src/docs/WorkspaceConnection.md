# WorkspaceConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ready** | **bool** |  | 
**reason** | **str** |  | 
**host** | **str** |  | 
**port** | **int** |  | 
**username** | **str** |  | 
**working_directory** | **str** |  | 
**host_key_fingerprint** | **str** |  | 

## Example

```python
from wodby.models.workspace_connection import WorkspaceConnection

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceConnection from a JSON string
workspace_connection_instance = WorkspaceConnection.from_json(json)
# print the JSON string representation of the object
print(WorkspaceConnection.to_json())

# convert the object into a dict
workspace_connection_dict = workspace_connection_instance.to_dict()
# create an instance of WorkspaceConnection from a dict
workspace_connection_from_dict = WorkspaceConnection.from_dict(workspace_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


