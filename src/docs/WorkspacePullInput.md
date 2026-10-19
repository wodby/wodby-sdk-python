# WorkspacePullInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scripts** | **bool** | Run the environment&#39;s post-deployment scripts after the pull. | [optional] [default to True]

## Example

```python
from wodby.models.workspace_pull_input import WorkspacePullInput

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspacePullInput from a JSON string
workspace_pull_input_instance = WorkspacePullInput.from_json(json)
# print the JSON string representation of the object
print(WorkspacePullInput.to_json())

# convert the object into a dict
workspace_pull_input_dict = workspace_pull_input_instance.to_dict()
# create an instance of WorkspacePullInput from a dict
workspace_pull_input_from_dict = WorkspacePullInput.from_dict(workspace_pull_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


