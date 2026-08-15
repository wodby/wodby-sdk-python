# AppAccessSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from wodby.models.app_access_setting import AppAccessSetting

# TODO update the JSON string below
json = "{}"
# create an instance of AppAccessSetting from a JSON string
app_access_setting_instance = AppAccessSetting.from_json(json)
# print the JSON string representation of the object
print(AppAccessSetting.to_json())

# convert the object into a dict
app_access_setting_dict = app_access_setting_instance.to_dict()
# create an instance of AppAccessSetting from a dict
app_access_setting_from_dict = AppAccessSetting.from_dict(app_access_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


