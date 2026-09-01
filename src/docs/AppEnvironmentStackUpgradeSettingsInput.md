# AppEnvironmentStackUpgradeSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versions** | **bool** |  | [optional] 
**replicas** | **bool** |  | [optional] 
**resources** | **bool** |  | [optional] 
**integrations** | **bool** |  | [optional] 
**services** | **bool** |  | [optional] 
**settings** | **bool** |  | [optional] 
**links** | **bool** |  | [optional] 
**tokens** | **bool** |  | [optional] 
**configs** | **bool** |  | [optional] 
**cron** | **bool** |  | [optional] 
**volumes** | **bool** |  | [optional] 
**main** | **bool** |  | [optional] 

## Example

```python
from wodby.models.app_environment_stack_upgrade_settings_input import AppEnvironmentStackUpgradeSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironmentStackUpgradeSettingsInput from a JSON string
app_environment_stack_upgrade_settings_input_instance = AppEnvironmentStackUpgradeSettingsInput.from_json(json)
# print the JSON string representation of the object
print(AppEnvironmentStackUpgradeSettingsInput.to_json())

# convert the object into a dict
app_environment_stack_upgrade_settings_input_dict = app_environment_stack_upgrade_settings_input_instance.to_dict()
# create an instance of AppEnvironmentStackUpgradeSettingsInput from a dict
app_environment_stack_upgrade_settings_input_from_dict = AppEnvironmentStackUpgradeSettingsInput.from_dict(app_environment_stack_upgrade_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


