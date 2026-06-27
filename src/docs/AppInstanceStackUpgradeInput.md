# AppInstanceStackUpgradeInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from wodby.models.app_instance_stack_upgrade_input import AppInstanceStackUpgradeInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstanceStackUpgradeInput from a JSON string
app_instance_stack_upgrade_input_instance = AppInstanceStackUpgradeInput.from_json(json)
# print the JSON string representation of the object
print(AppInstanceStackUpgradeInput.to_json())

# convert the object into a dict
app_instance_stack_upgrade_input_dict = app_instance_stack_upgrade_input_instance.to_dict()
# create an instance of AppInstanceStackUpgradeInput from a dict
app_instance_stack_upgrade_input_from_dict = AppInstanceStackUpgradeInput.from_dict(app_instance_stack_upgrade_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


