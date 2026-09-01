# AppEnvironmentSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_stack_upgrade** | [**AppInstanceAutoStackUpgradeSettingsInput**](AppInstanceAutoStackUpgradeSettingsInput.md) |  | [optional] 

## Example

```python
from wodby.models.app_environment_settings_input import AppEnvironmentSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironmentSettingsInput from a JSON string
app_environment_settings_input_instance = AppEnvironmentSettingsInput.from_json(json)
# print the JSON string representation of the object
print(AppEnvironmentSettingsInput.to_json())

# convert the object into a dict
app_environment_settings_input_dict = app_environment_settings_input_instance.to_dict()
# create an instance of AppEnvironmentSettingsInput from a dict
app_environment_settings_input_from_dict = AppEnvironmentSettingsInput.from_dict(app_environment_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


