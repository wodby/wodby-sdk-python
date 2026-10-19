# AppPortSettingInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**AppPortSettingName**](AppPortSettingName.md) |  | 
**value** | **str** |  | 

## Example

```python
from wodby.models.app_port_setting_input import AppPortSettingInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppPortSettingInput from a JSON string
app_port_setting_input_instance = AppPortSettingInput.from_json(json)
# print the JSON string representation of the object
print(AppPortSettingInput.to_json())

# convert the object into a dict
app_port_setting_input_dict = app_port_setting_input_instance.to_dict()
# create an instance of AppPortSettingInput from a dict
app_port_setting_input_from_dict = AppPortSettingInput.from_dict(app_port_setting_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


