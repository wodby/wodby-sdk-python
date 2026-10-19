# AppPortSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**List[AppPortSettingInput]**](AppPortSettingInput.md) | The complete list of settings. A setting left out is removed. | 

## Example

```python
from wodby.models.app_port_settings_input import AppPortSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppPortSettingsInput from a JSON string
app_port_settings_input_instance = AppPortSettingsInput.from_json(json)
# print the JSON string representation of the object
print(AppPortSettingsInput.to_json())

# convert the object into a dict
app_port_settings_input_dict = app_port_settings_input_instance.to_dict()
# create an instance of AppPortSettingsInput from a dict
app_port_settings_input_from_dict = AppPortSettingsInput.from_dict(app_port_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


