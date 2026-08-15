# AppAccessSettingInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from wodby.models.app_access_setting_input import AppAccessSettingInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppAccessSettingInput from a JSON string
app_access_setting_input_instance = AppAccessSettingInput.from_json(json)
# print the JSON string representation of the object
print(AppAccessSettingInput.to_json())

# convert the object into a dict
app_access_setting_input_dict = app_access_setting_input_instance.to_dict()
# create an instance of AppAccessSettingInput from a dict
app_access_setting_input_from_dict = AppAccessSettingInput.from_dict(app_access_setting_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


