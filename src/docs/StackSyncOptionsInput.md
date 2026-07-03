# StackSyncOptionsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_stack_helm_values** | **bool** |  | [optional] 
**delete_stack_env_vars** | **bool** |  | [optional] 
**delete_stack_tokens** | **bool** |  | [optional] 
**delete_stack_annotations** | **bool** |  | [optional] 
**delete_stack_services** | **bool** |  | [optional] 
**delete_stack_services_configuration** | **bool** |  | [optional] 

## Example

```python
from wodby.models.stack_sync_options_input import StackSyncOptionsInput

# TODO update the JSON string below
json = "{}"
# create an instance of StackSyncOptionsInput from a JSON string
stack_sync_options_input_instance = StackSyncOptionsInput.from_json(json)
# print the JSON string representation of the object
print(StackSyncOptionsInput.to_json())

# convert the object into a dict
stack_sync_options_input_dict = stack_sync_options_input_instance.to_dict()
# create an instance of StackSyncOptionsInput from a dict
stack_sync_options_input_from_dict = StackSyncOptionsInput.from_dict(stack_sync_options_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


