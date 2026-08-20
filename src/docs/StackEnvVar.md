# StackEnvVar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**value** | **str** |  | [optional] 
**value_secret_id** | **int** |  | [optional] 
**env_type** | **str** |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from wodby.models.stack_env_var import StackEnvVar

# TODO update the JSON string below
json = "{}"
# create an instance of StackEnvVar from a JSON string
stack_env_var_instance = StackEnvVar.from_json(json)
# print the JSON string representation of the object
print(StackEnvVar.to_json())

# convert the object into a dict
stack_env_var_dict = stack_env_var_instance.to_dict()
# create an instance of StackEnvVar from a dict
stack_env_var_from_dict = StackEnvVar.from_dict(stack_env_var_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


