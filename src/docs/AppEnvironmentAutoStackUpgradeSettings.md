# AppEnvironmentAutoStackUpgradeSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**upgrade_settings** | [**AppEnvironmentStackUpgradeSettings**](AppEnvironmentStackUpgradeSettings.md) |  | [optional] 
**time_window** | [**AutomationTimeWindow**](AutomationTimeWindow.md) |  | [optional] 

## Example

```python
from wodby.models.app_environment_auto_stack_upgrade_settings import AppEnvironmentAutoStackUpgradeSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironmentAutoStackUpgradeSettings from a JSON string
app_environment_auto_stack_upgrade_settings_instance = AppEnvironmentAutoStackUpgradeSettings.from_json(json)
# print the JSON string representation of the object
print(AppEnvironmentAutoStackUpgradeSettings.to_json())

# convert the object into a dict
app_environment_auto_stack_upgrade_settings_dict = app_environment_auto_stack_upgrade_settings_instance.to_dict()
# create an instance of AppEnvironmentAutoStackUpgradeSettings from a dict
app_environment_auto_stack_upgrade_settings_from_dict = AppEnvironmentAutoStackUpgradeSettings.from_dict(app_environment_auto_stack_upgrade_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


