# AppRouteSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**List[AppRouteSettingInput]**](AppRouteSettingInput.md) | The complete list of settings. A setting left out is removed. | 

## Example

```python
from wodby.models.app_route_settings_input import AppRouteSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppRouteSettingsInput from a JSON string
app_route_settings_input_instance = AppRouteSettingsInput.from_json(json)
# print the JSON string representation of the object
print(AppRouteSettingsInput.to_json())

# convert the object into a dict
app_route_settings_input_dict = app_route_settings_input_instance.to_dict()
# create an instance of AppRouteSettingsInput from a dict
app_route_settings_input_from_dict = AppRouteSettingsInput.from_dict(app_route_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


