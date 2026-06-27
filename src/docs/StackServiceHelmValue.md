# StackServiceHelmValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**stack_service_id** | **int** |  | 
**name** | **str** |  | 
**value** | **str** |  | [optional] 
**value_secret_id** | **int** |  | [optional] 
**env_type** | **str** |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from wodby.models.stack_service_helm_value import StackServiceHelmValue

# TODO update the JSON string below
json = "{}"
# create an instance of StackServiceHelmValue from a JSON string
stack_service_helm_value_instance = StackServiceHelmValue.from_json(json)
# print the JSON string representation of the object
print(StackServiceHelmValue.to_json())

# convert the object into a dict
stack_service_helm_value_dict = stack_service_helm_value_instance.to_dict()
# create an instance of StackServiceHelmValue from a dict
stack_service_helm_value_from_dict = StackServiceHelmValue.from_dict(stack_service_helm_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


