# AppServiceSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**app_service_id** | **int** |  | 
**name** | **str** |  | 
**value** | **str** |  | 
**secret** | **bool** |  | 
**has_value** | **bool** |  | 
**var** | **str** |  | 
**runtime** | **bool** |  | 
**build** | **bool** |  | 
**from_setting_id** | **int** |  | [optional] 

## Example

```python
from wodby.models.app_service_setting import AppServiceSetting

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceSetting from a JSON string
app_service_setting_instance = AppServiceSetting.from_json(json)
# print the JSON string representation of the object
print(AppServiceSetting.to_json())

# convert the object into a dict
app_service_setting_dict = app_service_setting_instance.to_dict()
# create an instance of AppServiceSetting from a dict
app_service_setting_from_dict = AppServiceSetting.from_dict(app_service_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


