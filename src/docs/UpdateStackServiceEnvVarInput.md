# UpdateStackServiceEnvVarInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**secret** | **bool** |  | 

## Example

```python
from wodby.models.update_stack_service_env_var_input import UpdateStackServiceEnvVarInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStackServiceEnvVarInput from a JSON string
update_stack_service_env_var_input_instance = UpdateStackServiceEnvVarInput.from_json(json)
# print the JSON string representation of the object
print(UpdateStackServiceEnvVarInput.to_json())

# convert the object into a dict
update_stack_service_env_var_input_dict = update_stack_service_env_var_input_instance.to_dict()
# create an instance of UpdateStackServiceEnvVarInput from a dict
update_stack_service_env_var_input_from_dict = UpdateStackServiceEnvVarInput.from_dict(update_stack_service_env_var_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


