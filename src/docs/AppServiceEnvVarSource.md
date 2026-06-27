# AppServiceEnvVarSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_service** | **bool** |  | 
**from_stack** | **bool** |  | 
**from_wodby** | **bool** |  | 
**setting** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**integration** | **str** |  | [optional] 

## Example

```python
from wodby.models.app_service_env_var_source import AppServiceEnvVarSource

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceEnvVarSource from a JSON string
app_service_env_var_source_instance = AppServiceEnvVarSource.from_json(json)
# print the JSON string representation of the object
print(AppServiceEnvVarSource.to_json())

# convert the object into a dict
app_service_env_var_source_dict = app_service_env_var_source_instance.to_dict()
# create an instance of AppServiceEnvVarSource from a dict
app_service_env_var_source_from_dict = AppServiceEnvVarSource.from_dict(app_service_env_var_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


