# GitAutoUpdateSettingsInput


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
from wodby.models.git_auto_update_settings_input import GitAutoUpdateSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of GitAutoUpdateSettingsInput from a JSON string
git_auto_update_settings_input_instance = GitAutoUpdateSettingsInput.from_json(json)
# print the JSON string representation of the object
print(GitAutoUpdateSettingsInput.to_json())

# convert the object into a dict
git_auto_update_settings_input_dict = git_auto_update_settings_input_instance.to_dict()
# create an instance of GitAutoUpdateSettingsInput from a dict
git_auto_update_settings_input_from_dict = GitAutoUpdateSettingsInput.from_dict(git_auto_update_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


