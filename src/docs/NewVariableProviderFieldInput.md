# NewVariableProviderFieldInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**label** | **str** |  | 
**variable** | **str** |  | 
**required** | **bool** |  | 
**secret** | **bool** |  | 

## Example

```python
from wodby.models.new_variable_provider_field_input import NewVariableProviderFieldInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewVariableProviderFieldInput from a JSON string
new_variable_provider_field_input_instance = NewVariableProviderFieldInput.from_json(json)
# print the JSON string representation of the object
print(NewVariableProviderFieldInput.to_json())

# convert the object into a dict
new_variable_provider_field_input_dict = new_variable_provider_field_input_instance.to_dict()
# create an instance of NewVariableProviderFieldInput from a dict
new_variable_provider_field_input_from_dict = NewVariableProviderFieldInput.from_dict(new_variable_provider_field_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


