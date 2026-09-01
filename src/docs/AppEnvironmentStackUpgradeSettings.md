# AppEnvironmentStackUpgradeSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versions** | **bool** |  | 
**replicas** | **bool** |  | 
**resources** | **bool** |  | 
**integrations** | **bool** |  | 
**services** | **bool** |  | 
**settings** | **bool** |  | 
**links** | **bool** |  | 
**tokens** | **bool** |  | 
**configs** | **bool** |  | 
**cron** | **bool** |  | 
**volumes** | **bool** |  | 
**main** | **bool** |  | 

## Example

```python
from wodby.models.app_environment_stack_upgrade_settings import AppEnvironmentStackUpgradeSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironmentStackUpgradeSettings from a JSON string
app_environment_stack_upgrade_settings_instance = AppEnvironmentStackUpgradeSettings.from_json(json)
# print the JSON string representation of the object
print(AppEnvironmentStackUpgradeSettings.to_json())

# convert the object into a dict
app_environment_stack_upgrade_settings_dict = app_environment_stack_upgrade_settings_instance.to_dict()
# create an instance of AppEnvironmentStackUpgradeSettings from a dict
app_environment_stack_upgrade_settings_from_dict = AppEnvironmentStackUpgradeSettings.from_dict(app_environment_stack_upgrade_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


