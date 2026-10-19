# WorkspaceGitChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | 
**original_path** | **str** | Previous path of a renamed or copied file. | [optional] 
**kind** | **str** |  | 
**staged** | **bool** | The index differs from HEAD for this path. | 
**unstaged** | **bool** | The working tree differs from the index for this path. | 

## Example

```python
from wodby.models.workspace_git_change import WorkspaceGitChange

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceGitChange from a JSON string
workspace_git_change_instance = WorkspaceGitChange.from_json(json)
# print the JSON string representation of the object
print(WorkspaceGitChange.to_json())

# convert the object into a dict
workspace_git_change_dict = workspace_git_change_instance.to_dict()
# create an instance of WorkspaceGitChange from a dict
workspace_git_change_from_dict = WorkspaceGitChange.from_dict(workspace_git_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


