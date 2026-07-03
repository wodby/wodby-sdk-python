# AppInstanceSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_stack_upgrade** | [**AppInstanceAutoStackUpgradeSettingsInput**](AppInstanceAutoStackUpgradeSettingsInput.md) |  | [optional] 

## Example

```python
from wodby.models.app_instance_settings_input import AppInstanceSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstanceSettingsInput from a JSON string
app_instance_settings_input_instance = AppInstanceSettingsInput.from_json(json)
# print the JSON string representation of the object
print(AppInstanceSettingsInput.to_json())

# convert the object into a dict
app_instance_settings_input_dict = app_instance_settings_input_instance.to_dict()
# create an instance of AppInstanceSettingsInput from a dict
app_instance_settings_input_from_dict = AppInstanceSettingsInput.from_dict(app_instance_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


