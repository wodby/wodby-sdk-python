# StackServiceEnvVar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**stack_service_id** | **int** |  | 
**workload** | **str** |  | 
**container** | **str** |  | 
**name** | **str** |  | 
**value** | **str** |  | [optional] 
**value_secret_id** | **int** |  | [optional] 
**env_type** | **str** |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from wodby.models.stack_service_env_var import StackServiceEnvVar

# TODO update the JSON string below
json = "{}"
# create an instance of StackServiceEnvVar from a JSON string
stack_service_env_var_instance = StackServiceEnvVar.from_json(json)
# print the JSON string representation of the object
print(StackServiceEnvVar.to_json())

# convert the object into a dict
stack_service_env_var_dict = stack_service_env_var_instance.to_dict()
# create an instance of StackServiceEnvVar from a dict
stack_service_env_var_from_dict = StackServiceEnvVar.from_dict(stack_service_env_var_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


