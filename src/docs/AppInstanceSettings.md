# AppInstanceSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_stack_upgrade** | [**AppInstanceAutoStackUpgradeSettings**](AppInstanceAutoStackUpgradeSettings.md) |  | [optional] 

## Example

```python
from wodby.models.app_instance_settings import AppInstanceSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstanceSettings from a JSON string
app_instance_settings_instance = AppInstanceSettings.from_json(json)
# print the JSON string representation of the object
print(AppInstanceSettings.to_json())

# convert the object into a dict
app_instance_settings_dict = app_instance_settings_instance.to_dict()
# create an instance of AppInstanceSettings from a dict
app_instance_settings_from_dict = AppInstanceSettings.from_dict(app_instance_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


