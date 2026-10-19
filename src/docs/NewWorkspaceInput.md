# NewWorkspaceInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** |  | 
**storage_class_name** | **str** | Storage class for the workspace code and home volumes. Every Pod that mounts the code then runs on one node. Omit both storage fields to use the cluster&#39;s default storage class. Not allowed with storageServiceName. | [optional] 
**storage_service_name** | **str** | Enabled storage service in the selected stack that shares the workspace files across nodes. Not allowed with storageClassName. | [optional] 
**code_size** | **int** |  | [optional] [default to 10]
**home_size** | **int** |  | [optional] [default to 5]

## Example

```python
from wodby.models.new_workspace_input import NewWorkspaceInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewWorkspaceInput from a JSON string
new_workspace_input_instance = NewWorkspaceInput.from_json(json)
# print the JSON string representation of the object
print(NewWorkspaceInput.to_json())

# convert the object into a dict
new_workspace_input_dict = new_workspace_input_instance.to_dict()
# create an instance of NewWorkspaceInput from a dict
new_workspace_input_from_dict = NewWorkspaceInput.from_dict(new_workspace_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


