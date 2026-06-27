# NewAppServiceEnvVarInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workload** | **str** |  | [optional] 
**container** | **str** |  | [optional] 
**name** | **str** |  | 
**value** | **str** |  | 
**secret** | **bool** |  | 
**runtime** | **bool** |  | [optional] 
**build** | **bool** |  | [optional] 

## Example

```python
from wodby.models.new_app_service_env_var_input import NewAppServiceEnvVarInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewAppServiceEnvVarInput from a JSON string
new_app_service_env_var_input_instance = NewAppServiceEnvVarInput.from_json(json)
# print the JSON string representation of the object
print(NewAppServiceEnvVarInput.to_json())

# convert the object into a dict
new_app_service_env_var_input_dict = new_app_service_env_var_input_instance.to_dict()
# create an instance of NewAppServiceEnvVarInput from a dict
new_app_service_env_var_input_from_dict = NewAppServiceEnvVarInput.from_dict(new_app_service_env_var_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


