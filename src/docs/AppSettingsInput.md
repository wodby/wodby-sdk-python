# AppSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_environments** | [**AppPreviewEnvironmentsSettingsInput**](AppPreviewEnvironmentsSettingsInput.md) |  | [optional] 

## Example

```python
from wodby.models.app_settings_input import AppSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppSettingsInput from a JSON string
app_settings_input_instance = AppSettingsInput.from_json(json)
# print the JSON string representation of the object
print(AppSettingsInput.to_json())

# convert the object into a dict
app_settings_input_dict = app_settings_input_instance.to_dict()
# create an instance of AppSettingsInput from a dict
app_settings_input_from_dict = AppSettingsInput.from_dict(app_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


