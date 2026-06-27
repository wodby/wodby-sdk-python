# StackServiceInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replicas** | **int** |  | [optional] 
**required** | **bool** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**main** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**build_source** | [**BuildSourceInput**](BuildSourceInput.md) |  | [optional] 

## Example

```python
from wodby.models.stack_service_input import StackServiceInput

# TODO update the JSON string below
json = "{}"
# create an instance of StackServiceInput from a JSON string
stack_service_input_instance = StackServiceInput.from_json(json)
# print the JSON string representation of the object
print(StackServiceInput.to_json())

# convert the object into a dict
stack_service_input_dict = stack_service_input_instance.to_dict()
# create an instance of StackServiceInput from a dict
stack_service_input_from_dict = StackServiceInput.from_dict(stack_service_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


