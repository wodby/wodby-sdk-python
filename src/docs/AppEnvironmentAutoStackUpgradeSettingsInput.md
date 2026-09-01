# AppEnvironmentAutoStackUpgradeSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**upgrade_settings** | [**AppEnvironmentStackUpgradeSettingsInput**](AppEnvironmentStackUpgradeSettingsInput.md) |  | [optional] 
**time_window** | [**AutomationTimeWindowInput**](AutomationTimeWindowInput.md) |  | [optional] 

## Example

```python
from wodby.models.app_environment_auto_stack_upgrade_settings_input import AppEnvironmentAutoStackUpgradeSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironmentAutoStackUpgradeSettingsInput from a JSON string
app_environment_auto_stack_upgrade_settings_input_instance = AppEnvironmentAutoStackUpgradeSettingsInput.from_json(json)
# print the JSON string representation of the object
print(AppEnvironmentAutoStackUpgradeSettingsInput.to_json())

# convert the object into a dict
app_environment_auto_stack_upgrade_settings_input_dict = app_environment_auto_stack_upgrade_settings_input_instance.to_dict()
# create an instance of AppEnvironmentAutoStackUpgradeSettingsInput from a dict
app_environment_auto_stack_upgrade_settings_input_from_dict = AppEnvironmentAutoStackUpgradeSettingsInput.from_dict(app_environment_auto_stack_upgrade_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


