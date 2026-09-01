# AppEnvironmentSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_stack_upgrade** | [**AppEnvironmentAutoStackUpgradeSettings**](AppEnvironmentAutoStackUpgradeSettings.md) |  | [optional] 

## Example

```python
from wodby.models.app_environment_settings import AppEnvironmentSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironmentSettings from a JSON string
app_environment_settings_instance = AppEnvironmentSettings.from_json(json)
# print the JSON string representation of the object
print(AppEnvironmentSettings.to_json())

# convert the object into a dict
app_environment_settings_dict = app_environment_settings_instance.to_dict()
# create an instance of AppEnvironmentSettings from a dict
app_environment_settings_from_dict = AppEnvironmentSettings.from_dict(app_environment_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


