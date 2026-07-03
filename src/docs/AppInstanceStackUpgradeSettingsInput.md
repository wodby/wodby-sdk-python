# AppInstanceStackUpgradeSettingsInput


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
from wodby.models.app_instance_stack_upgrade_settings_input import AppInstanceStackUpgradeSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstanceStackUpgradeSettingsInput from a JSON string
app_instance_stack_upgrade_settings_input_instance = AppInstanceStackUpgradeSettingsInput.from_json(json)
# print the JSON string representation of the object
print(AppInstanceStackUpgradeSettingsInput.to_json())

# convert the object into a dict
app_instance_stack_upgrade_settings_input_dict = app_instance_stack_upgrade_settings_input_instance.to_dict()
# create an instance of AppInstanceStackUpgradeSettingsInput from a dict
app_instance_stack_upgrade_settings_input_from_dict = AppInstanceStackUpgradeSettingsInput.from_dict(app_instance_stack_upgrade_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


