# NewStackHelmValueInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 
**secret** | **bool** |  | 
**env_type** | **str** | Limit the value to app environments of this type. | [optional] 

## Example

```python
from wodby.models.new_stack_helm_value_input import NewStackHelmValueInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewStackHelmValueInput from a JSON string
new_stack_helm_value_input_instance = NewStackHelmValueInput.from_json(json)
# print the JSON string representation of the object
print(NewStackHelmValueInput.to_json())

# convert the object into a dict
new_stack_helm_value_input_dict = new_stack_helm_value_input_instance.to_dict()
# create an instance of NewStackHelmValueInput from a dict
new_stack_helm_value_input_from_dict = NewStackHelmValueInput.from_dict(new_stack_helm_value_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


