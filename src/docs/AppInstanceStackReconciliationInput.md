# AppInstanceStackReconciliationInput


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
from wodby.models.app_instance_stack_reconciliation_input import AppInstanceStackReconciliationInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstanceStackReconciliationInput from a JSON string
app_instance_stack_reconciliation_input_instance = AppInstanceStackReconciliationInput.from_json(json)
# print the JSON string representation of the object
print(AppInstanceStackReconciliationInput.to_json())

# convert the object into a dict
app_instance_stack_reconciliation_input_dict = app_instance_stack_reconciliation_input_instance.to_dict()
# create an instance of AppInstanceStackReconciliationInput from a dict
app_instance_stack_reconciliation_input_from_dict = AppInstanceStackReconciliationInput.from_dict(app_instance_stack_reconciliation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


