# UpdateStackEnvVarInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**secret** | **bool** |  | 

## Example

```python
from wodby.models.update_stack_env_var_input import UpdateStackEnvVarInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStackEnvVarInput from a JSON string
update_stack_env_var_input_instance = UpdateStackEnvVarInput.from_json(json)
# print the JSON string representation of the object
print(UpdateStackEnvVarInput.to_json())

# convert the object into a dict
update_stack_env_var_input_dict = update_stack_env_var_input_instance.to_dict()
# create an instance of UpdateStackEnvVarInput from a dict
update_stack_env_var_input_from_dict = UpdateStackEnvVarInput.from_dict(update_stack_env_var_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


