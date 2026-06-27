# UpdateAppServiceEnvVarInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**secret** | **bool** |  | 
**runtime** | **bool** |  | [optional] 
**build** | **bool** |  | [optional] 

## Example

```python
from wodby.models.update_app_service_env_var_input import UpdateAppServiceEnvVarInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAppServiceEnvVarInput from a JSON string
update_app_service_env_var_input_instance = UpdateAppServiceEnvVarInput.from_json(json)
# print the JSON string representation of the object
print(UpdateAppServiceEnvVarInput.to_json())

# convert the object into a dict
update_app_service_env_var_input_dict = update_app_service_env_var_input_instance.to_dict()
# create an instance of UpdateAppServiceEnvVarInput from a dict
update_app_service_env_var_input_from_dict = UpdateAppServiceEnvVarInput.from_dict(update_app_service_env_var_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


