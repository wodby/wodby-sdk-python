# RemoteGitRepo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from wodby.models.remote_git_repo import RemoteGitRepo

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteGitRepo from a JSON string
remote_git_repo_instance = RemoteGitRepo.from_json(json)
# print the JSON string representation of the object
print(RemoteGitRepo.to_json())

# convert the object into a dict
remote_git_repo_dict = remote_git_repo_instance.to_dict()
# create an instance of RemoteGitRepo from a dict
remote_git_repo_from_dict = RemoteGitRepo.from_dict(remote_git_repo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


