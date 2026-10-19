# AppRouteSettingInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**AppRouteSettingName**](AppRouteSettingName.md) |  | 
**value** | **str** |  | 

## Example

```python
from wodby.models.app_route_setting_input import AppRouteSettingInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppRouteSettingInput from a JSON string
app_route_setting_input_instance = AppRouteSettingInput.from_json(json)
# print the JSON string representation of the object
print(AppRouteSettingInput.to_json())

# convert the object into a dict
app_route_setting_input_dict = app_route_setting_input_instance.to_dict()
# create an instance of AppRouteSettingInput from a dict
app_route_setting_input_from_dict = AppRouteSettingInput.from_dict(app_route_setting_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


