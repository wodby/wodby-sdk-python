# AppEnvironmentStackUpgradeInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment** | **bool** | Build affected services when required and deploy the upgraded stack configuration. | [optional] [default to True]
**rebuild** | **bool** | Build services whose build inputs the upgrade changes before deploying them. When false, those services are deployed with their current build and stay marked as needing a rebuild until their next build; a service with no build to reuse is still built. Ignored when deployment is false. | [optional] [default to True]
**versions** | **bool** |  | 
**replicas** | **bool** |  | 
**resources** | **bool** |  | 
**integrations** | **bool** |  | 
**services** | **bool** |  | 
**settings** | **bool** |  | 
**links** | **bool** |  | 
**tokens** | **bool** |  | 
**configs** | **bool** |  | 
**cron** | **bool** |  | 
**volumes** | **bool** |  | 
**main** | **bool** |  | 

## Example

```python
from wodby.models.app_environment_stack_upgrade_input import AppEnvironmentStackUpgradeInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironmentStackUpgradeInput from a JSON string
app_environment_stack_upgrade_input_instance = AppEnvironmentStackUpgradeInput.from_json(json)
# print the JSON string representation of the object
print(AppEnvironmentStackUpgradeInput.to_json())

# convert the object into a dict
app_environment_stack_upgrade_input_dict = app_environment_stack_upgrade_input_instance.to_dict()
# create an instance of AppEnvironmentStackUpgradeInput from a dict
app_environment_stack_upgrade_input_from_dict = AppEnvironmentStackUpgradeInput.from_dict(app_environment_stack_upgrade_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


