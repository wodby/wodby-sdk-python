# GitRepoUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from wodby.models.git_repo_usage import GitRepoUsage

# TODO update the JSON string below
json = "{}"
# create an instance of GitRepoUsage from a JSON string
git_repo_usage_instance = GitRepoUsage.from_json(json)
# print the JSON string representation of the object
print(GitRepoUsage.to_json())

# convert the object into a dict
git_repo_usage_dict = git_repo_usage_instance.to_dict()
# create an instance of GitRepoUsage from a dict
git_repo_usage_from_dict = GitRepoUsage.from_dict(git_repo_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


