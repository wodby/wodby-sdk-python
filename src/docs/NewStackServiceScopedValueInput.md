# NewStackServiceScopedValueInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 
**secret** | **bool** |  | 
**env_type** | **str** |  | [optional] 

## Example

```python
from wodby.models.new_stack_service_scoped_value_input import NewStackServiceScopedValueInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewStackServiceScopedValueInput from a JSON string
new_stack_service_scoped_value_input_instance = NewStackServiceScopedValueInput.from_json(json)
# print the JSON string representation of the object
print(NewStackServiceScopedValueInput.to_json())

# convert the object into a dict
new_stack_service_scoped_value_input_dict = new_stack_service_scoped_value_input_instance.to_dict()
# create an instance of NewStackServiceScopedValueInput from a dict
new_stack_service_scoped_value_input_from_dict = NewStackServiceScopedValueInput.from_dict(new_stack_service_scoped_value_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


