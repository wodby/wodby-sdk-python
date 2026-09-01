# NewAppEnvironmentInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **int** |  | 
**environment_name** | **str** |  | 
**environment_title** | **str** | Defaults to environmentName when omitted. | [optional] 
**environment_type** | **str** |  | 
**domain** | **str** | Defaults to environmentName.appName.orgDomain when omitted. | [optional] 
**stack_rev_id** | **int** |  | 
**services** | [**List[NewAppServiceInput]**](NewAppServiceInput.md) | Defaults to the stack revision&#39;s service defaults when omitted. | [optional] 
**cluster_id** | **int** |  | [optional] 
**ci_integration_id** | **int** |  | [optional] 
**registry_integration_id** | **int** |  | [optional] 
**defer_initial_deployment** | **bool** |  | [optional] [default to False]
**settings** | [**AppEnvironmentSettingsInput**](AppEnvironmentSettingsInput.md) |  | [optional] 
**access** | [**NewAppEnvironmentAccessInput**](NewAppEnvironmentAccessInput.md) |  | [optional] 

## Example

```python
from wodby.models.new_app_environment_input import NewAppEnvironmentInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewAppEnvironmentInput from a JSON string
new_app_environment_input_instance = NewAppEnvironmentInput.from_json(json)
# print the JSON string representation of the object
print(NewAppEnvironmentInput.to_json())

# convert the object into a dict
new_app_environment_input_dict = new_app_environment_input_instance.to_dict()
# create an instance of NewAppEnvironmentInput from a dict
new_app_environment_input_from_dict = NewAppEnvironmentInput.from_dict(new_app_environment_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


