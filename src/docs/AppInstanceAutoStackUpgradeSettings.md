# AppInstanceAutoStackUpgradeSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**upgrade_settings** | [**AppInstanceStackUpgradeSettings**](AppInstanceStackUpgradeSettings.md) |  | [optional] 

## Example

```python
from wodby.models.app_instance_auto_stack_upgrade_settings import AppInstanceAutoStackUpgradeSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstanceAutoStackUpgradeSettings from a JSON string
app_instance_auto_stack_upgrade_settings_instance = AppInstanceAutoStackUpgradeSettings.from_json(json)
# print the JSON string representation of the object
print(AppInstanceAutoStackUpgradeSettings.to_json())

# convert the object into a dict
app_instance_auto_stack_upgrade_settings_dict = app_instance_auto_stack_upgrade_settings_instance.to_dict()
# create an instance of AppInstanceAutoStackUpgradeSettings from a dict
app_instance_auto_stack_upgrade_settings_from_dict = AppInstanceAutoStackUpgradeSettings.from_dict(app_instance_auto_stack_upgrade_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


