# AppPortSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | [**AppPortSettingName**](AppPortSettingName.md) |  | 
**value** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.app_port_setting import AppPortSetting

# TODO update the JSON string below
json = "{}"
# create an instance of AppPortSetting from a JSON string
app_port_setting_instance = AppPortSetting.from_json(json)
# print the JSON string representation of the object
print(AppPortSetting.to_json())

# convert the object into a dict
app_port_setting_dict = app_port_setting_instance.to_dict()
# create an instance of AppPortSetting from a dict
app_port_setting_from_dict = AppPortSetting.from_dict(app_port_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


