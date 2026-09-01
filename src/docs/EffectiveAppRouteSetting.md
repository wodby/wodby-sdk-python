# EffectiveAppRouteSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**AppRouteSettingName**](AppRouteSettingName.md) |  | 
**value** | **str** |  | 
**source** | [**AppRouteSettingSource**](AppRouteSettingSource.md) |  | 

## Example

```python
from wodby.models.effective_app_route_setting import EffectiveAppRouteSetting

# TODO update the JSON string below
json = "{}"
# create an instance of EffectiveAppRouteSetting from a JSON string
effective_app_route_setting_instance = EffectiveAppRouteSetting.from_json(json)
# print the JSON string representation of the object
print(EffectiveAppRouteSetting.to_json())

# convert the object into a dict
effective_app_route_setting_dict = effective_app_route_setting_instance.to_dict()
# create an instance of EffectiveAppRouteSetting from a dict
effective_app_route_setting_from_dict = EffectiveAppRouteSetting.from_dict(effective_app_route_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


