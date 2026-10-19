# WorkspaceGitStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | False when the state cannot be read; reason explains why and the other fields are omitted. | 
**reason** | **str** |  | [optional] 
**branch** | **str** | Current branch; omitted for a detached HEAD. | [optional] 
**upstream** | **str** | Upstream branch that the current branch tracks. | [optional] 
**ahead** | **int** | Commits on the current branch that its upstream does not have. | [optional] 
**behind** | **int** | Commits on the upstream that the current branch does not have. | [optional] 
**commit** | **str** | HEAD commit; omitted before the first commit. | [optional] 
**commit_subject** | **str** |  | [optional] 
**committed_at** | **datetime** |  | [optional] 
**changes** | [**List[WorkspaceGitChange]**](WorkspaceGitChange.md) | Uncommitted changes, including untracked files. | 
**truncated** | **bool** | True when more changes exist than listed. | 
**checked_at** | **datetime** |  | 

## Example

```python
from wodby.models.workspace_git_status import WorkspaceGitStatus

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceGitStatus from a JSON string
workspace_git_status_instance = WorkspaceGitStatus.from_json(json)
# print the JSON string representation of the object
print(WorkspaceGitStatus.to_json())

# convert the object into a dict
workspace_git_status_dict = workspace_git_status_instance.to_dict()
# create an instance of WorkspaceGitStatus from a dict
workspace_git_status_from_dict = WorkspaceGitStatus.from_dict(workspace_git_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


