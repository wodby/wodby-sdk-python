# WorkspaceGitDiff


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | False when the diff cannot be read; reason explains why and diff is empty. | 
**reason** | **str** |  | [optional] 
**path** | **str** |  | 
**diff** | **str** | Unified diff of staged and unstaged changes. Empty when the file does not differ. | 
**binary** | **bool** | True for a file Git does not show line by line. | 
**truncated** | **bool** | True when the diff is longer than what is returned. | 

## Example

```python
from wodby.models.workspace_git_diff import WorkspaceGitDiff

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceGitDiff from a JSON string
workspace_git_diff_instance = WorkspaceGitDiff.from_json(json)
# print the JSON string representation of the object
print(WorkspaceGitDiff.to_json())

# convert the object into a dict
workspace_git_diff_dict = workspace_git_diff_instance.to_dict()
# create an instance of WorkspaceGitDiff from a dict
workspace_git_diff_from_dict = WorkspaceGitDiff.from_dict(workspace_git_diff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


