# SyncStackWithOriginInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_stack_helm_values** | **bool** |  | [optional] 
**delete_stack_env_vars** | **bool** |  | [optional] 
**delete_stack_tokens** | **bool** |  | [optional] 
**delete_stack_annotations** | **bool** |  | [optional] 
**delete_stack_services** | **bool** |  | [optional] 
**delete_stack_services_configuration** | **bool** |  | [optional] 
**update_stack_services** | **bool** | Let the sync update existing stack services to the service version the origin uses when the origin&#39;s changes need it. Without it, such a sync fails with an error that lists those stack services. | [optional] 

## Example

```python
from wodby.models.sync_stack_with_origin_input import SyncStackWithOriginInput

# TODO update the JSON string below
json = "{}"
# create an instance of SyncStackWithOriginInput from a JSON string
sync_stack_with_origin_input_instance = SyncStackWithOriginInput.from_json(json)
# print the JSON string representation of the object
print(SyncStackWithOriginInput.to_json())

# convert the object into a dict
sync_stack_with_origin_input_dict = sync_stack_with_origin_input_instance.to_dict()
# create an instance of SyncStackWithOriginInput from a dict
sync_stack_with_origin_input_from_dict = SyncStackWithOriginInput.from_dict(sync_stack_with_origin_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


