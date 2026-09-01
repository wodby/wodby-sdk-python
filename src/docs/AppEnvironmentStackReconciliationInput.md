# AppEnvironmentStackReconciliationInput


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
from wodby.models.app_environment_stack_reconciliation_input import AppEnvironmentStackReconciliationInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironmentStackReconciliationInput from a JSON string
app_environment_stack_reconciliation_input_instance = AppEnvironmentStackReconciliationInput.from_json(json)
# print the JSON string representation of the object
print(AppEnvironmentStackReconciliationInput.to_json())

# convert the object into a dict
app_environment_stack_reconciliation_input_dict = app_environment_stack_reconciliation_input_instance.to_dict()
# create an instance of AppEnvironmentStackReconciliationInput from a dict
app_environment_stack_reconciliation_input_from_dict = AppEnvironmentStackReconciliationInput.from_dict(app_environment_stack_reconciliation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


