# NewStackEnvVarInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 
**secret** | **bool** |  | 
**env_type** | **str** |  | [optional] 

## Example

```python
from wodby.models.new_stack_env_var_input import NewStackEnvVarInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewStackEnvVarInput from a JSON string
new_stack_env_var_input_instance = NewStackEnvVarInput.from_json(json)
# print the JSON string representation of the object
print(NewStackEnvVarInput.to_json())

# convert the object into a dict
new_stack_env_var_input_dict = new_stack_env_var_input_instance.to_dict()
# create an instance of NewStackEnvVarInput from a dict
new_stack_env_var_input_from_dict = NewStackEnvVarInput.from_dict(new_stack_env_var_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


