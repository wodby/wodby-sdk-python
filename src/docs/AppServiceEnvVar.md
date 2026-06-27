# AppServiceEnvVar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**app_service_id** | **int** |  | 
**workload** | **str** |  | 
**container** | **str** |  | 
**name** | **str** |  | 
**value** | **str** |  | 
**value_secret_id** | **int** |  | [optional] 
**runtime** | **bool** |  | 
**build** | **bool** |  | 
**env_type** | **str** |  | [optional] 
**source** | [**AppServiceEnvVarSource**](AppServiceEnvVarSource.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from wodby.models.app_service_env_var import AppServiceEnvVar

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceEnvVar from a JSON string
app_service_env_var_instance = AppServiceEnvVar.from_json(json)
# print the JSON string representation of the object
print(AppServiceEnvVar.to_json())

# convert the object into a dict
app_service_env_var_dict = app_service_env_var_instance.to_dict()
# create an instance of AppServiceEnvVar from a dict
app_service_env_var_from_dict = AppServiceEnvVar.from_dict(app_service_env_var_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


