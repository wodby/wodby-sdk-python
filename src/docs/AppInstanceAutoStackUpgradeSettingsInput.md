# AppInstanceAutoStackUpgradeSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**upgrade_settings** | [**AppInstanceStackUpgradeSettingsInput**](AppInstanceStackUpgradeSettingsInput.md) |  | [optional] 

## Example

```python
from wodby.models.app_instance_auto_stack_upgrade_settings_input import AppInstanceAutoStackUpgradeSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstanceAutoStackUpgradeSettingsInput from a JSON string
app_instance_auto_stack_upgrade_settings_input_instance = AppInstanceAutoStackUpgradeSettingsInput.from_json(json)
# print the JSON string representation of the object
print(AppInstanceAutoStackUpgradeSettingsInput.to_json())

# convert the object into a dict
app_instance_auto_stack_upgrade_settings_input_dict = app_instance_auto_stack_upgrade_settings_input_instance.to_dict()
# create an instance of AppInstanceAutoStackUpgradeSettingsInput from a dict
app_instance_auto_stack_upgrade_settings_input_from_dict = AppInstanceAutoStackUpgradeSettingsInput.from_dict(app_instance_auto_stack_upgrade_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


