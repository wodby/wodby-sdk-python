# GitRepoUsages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**services** | [**List[GitRepoUsage]**](GitRepoUsage.md) |  | 
**stacks** | [**List[GitRepoUsage]**](GitRepoUsage.md) |  | 
**providers** | [**List[GitRepoUsage]**](GitRepoUsage.md) |  | 

## Example

```python
from wodby.models.git_repo_usages import GitRepoUsages

# TODO update the JSON string below
json = "{}"
# create an instance of GitRepoUsages from a JSON string
git_repo_usages_instance = GitRepoUsages.from_json(json)
# print the JSON string representation of the object
print(GitRepoUsages.to_json())

# convert the object into a dict
git_repo_usages_dict = git_repo_usages_instance.to_dict()
# create an instance of GitRepoUsages from a dict
git_repo_usages_from_dict = GitRepoUsages.from_dict(git_repo_usages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


