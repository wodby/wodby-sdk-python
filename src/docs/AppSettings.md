# AppSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_environments** | [**AppPreviewEnvironmentsSettings**](AppPreviewEnvironmentsSettings.md) |  | 

## Example

```python
from wodby.models.app_settings import AppSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AppSettings from a JSON string
app_settings_instance = AppSettings.from_json(json)
# print the JSON string representation of the object
print(AppSettings.to_json())

# convert the object into a dict
app_settings_dict = app_settings_instance.to_dict()
# create an instance of AppSettings from a dict
app_settings_from_dict = AppSettings.from_dict(app_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


