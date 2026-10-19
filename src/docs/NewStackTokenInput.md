# NewStackTokenInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** | Leave it out to generate a value from regex. | [optional] 
**secret** | **bool** |  | 
**regex** | **str** | Pattern used to generate the value for each app environment. | [optional] 
**env_type** | **str** | Limit the value to app environments of this type. | [optional] 

## Example

```python
from wodby.models.new_stack_token_input import NewStackTokenInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewStackTokenInput from a JSON string
new_stack_token_input_instance = NewStackTokenInput.from_json(json)
# print the JSON string representation of the object
print(NewStackTokenInput.to_json())

# convert the object into a dict
new_stack_token_input_dict = new_stack_token_input_instance.to_dict()
# create an instance of NewStackTokenInput from a dict
new_stack_token_input_from_dict = NewStackTokenInput.from_dict(new_stack_token_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


