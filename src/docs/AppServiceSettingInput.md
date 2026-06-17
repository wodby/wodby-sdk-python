# AppServiceSettingInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from wodby.models.app_service_setting_input import AppServiceSettingInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceSettingInput from a JSON string
app_service_setting_input_instance = AppServiceSettingInput.from_json(json)
# print the JSON string representation of the object
print(AppServiceSettingInput.to_json())

# convert the object into a dict
app_service_setting_input_dict = app_service_setting_input_instance.to_dict()
# create an instance of AppServiceSettingInput from a dict
app_service_setting_input_from_dict = AppServiceSettingInput.from_dict(app_service_setting_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


