# StackSyncOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_stack_helm_values** | **bool** |  | 
**delete_stack_env_vars** | **bool** |  | 
**delete_stack_tokens** | **bool** |  | 
**delete_stack_annotations** | **bool** |  | 
**delete_stack_services** | **bool** |  | 
**delete_stack_services_configuration** | **bool** |  | 

## Example

```python
from wodby.models.stack_sync_options import StackSyncOptions

# TODO update the JSON string below
json = "{}"
# create an instance of StackSyncOptions from a JSON string
stack_sync_options_instance = StackSyncOptions.from_json(json)
# print the JSON string representation of the object
print(StackSyncOptions.to_json())

# convert the object into a dict
stack_sync_options_dict = stack_sync_options_instance.to_dict()
# create an instance of StackSyncOptions from a dict
stack_sync_options_from_dict = StackSyncOptions.from_dict(stack_sync_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


