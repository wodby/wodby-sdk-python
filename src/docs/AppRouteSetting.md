# AppRouteSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**app_instance_id** | **int** |  | 
**route_id** | **int** |  | 
**default** | **bool** |  | 
**name** | [**AppRouteSettingName**](AppRouteSettingName.md) |  | 
**value** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.app_route_setting import AppRouteSetting

# TODO update the JSON string below
json = "{}"
# create an instance of AppRouteSetting from a JSON string
app_route_setting_instance = AppRouteSetting.from_json(json)
# print the JSON string representation of the object
print(AppRouteSetting.to_json())

# convert the object into a dict
app_route_setting_dict = app_route_setting_instance.to_dict()
# create an instance of AppRouteSetting from a dict
app_route_setting_from_dict = AppRouteSetting.from_dict(app_route_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


