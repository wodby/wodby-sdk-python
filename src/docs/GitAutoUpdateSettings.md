# GitAutoUpdateSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**branches** | **bool** |  | 
**semver_tags** | **bool** |  | 
**allow_patch** | **bool** |  | 
**allow_minor** | **bool** |  | 
**allow_major** | **bool** |  | 

## Example

```python
from wodby.models.git_auto_update_settings import GitAutoUpdateSettings

# TODO update the JSON string below
json = "{}"
# create an instance of GitAutoUpdateSettings from a JSON string
git_auto_update_settings_instance = GitAutoUpdateSettings.from_json(json)
# print the JSON string representation of the object
print(GitAutoUpdateSettings.to_json())

# convert the object into a dict
git_auto_update_settings_dict = git_auto_update_settings_instance.to_dict()
# create an instance of GitAutoUpdateSettings from a dict
git_auto_update_settings_from_dict = GitAutoUpdateSettings.from_dict(git_auto_update_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


