# StackHelmValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**value** | **str** | Omitted for secret values. | [optional] 
**value_secret_id** | **int** |  | [optional] 
**env_type** | **str** | Limit the value to app environments of this type. | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from wodby.models.stack_helm_value import StackHelmValue

# TODO update the JSON string below
json = "{}"
# create an instance of StackHelmValue from a JSON string
stack_helm_value_instance = StackHelmValue.from_json(json)
# print the JSON string representation of the object
print(StackHelmValue.to_json())

# convert the object into a dict
stack_helm_value_dict = stack_helm_value_instance.to_dict()
# create an instance of StackHelmValue from a dict
stack_helm_value_from_dict = StackHelmValue.from_dict(stack_helm_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


