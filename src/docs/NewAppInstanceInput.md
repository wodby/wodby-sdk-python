# NewAppInstanceInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **int** |  | 
**instance_name** | **str** |  | 
**instance_title** | **str** | Defaults to instanceName when omitted. | [optional] 
**domain** | **str** | Defaults to instanceName.appName.orgDomain when omitted. | [optional] 
**stack_rev_id** | **int** |  | 
**services** | [**List[NewAppServiceInput]**](NewAppServiceInput.md) | Defaults to the stack revision&#39;s service defaults when omitted. | [optional] 
**cluster_id** | **int** |  | [optional] 
**env_id** | **int** |  | 
**ci_integration_id** | **int** | Omit or use null to inherit the organization default, use 0 for the built-in CI service, or use an accessible CI integration ID. A project-owned integration must be shared with the app&#39;s project. | [optional] 
**registry_integration_id** | **int** | Omit or use null to inherit the organization default, use 0 for the built-in registry, or use an accessible registry integration ID. A project-owned integration must be shared with the app&#39;s project. | [optional] 
**defer_initial_deployment** | **bool** | Defers the automatic initial build and deployment while preserving app instance initialization. Intended for automation that configures the instance before explicitly starting its first build. | [optional] [default to False]
**settings** | [**AppInstanceSettingsInput**](AppInstanceSettingsInput.md) |  | [optional] 
**access** | [**NewAppInstanceAccessInput**](NewAppInstanceAccessInput.md) |  | [optional] 

## Example

```python
from wodby.models.new_app_instance_input import NewAppInstanceInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewAppInstanceInput from a JSON string
new_app_instance_input_instance = NewAppInstanceInput.from_json(json)
# print the JSON string representation of the object
print(NewAppInstanceInput.to_json())

# convert the object into a dict
new_app_instance_input_dict = new_app_instance_input_instance.to_dict()
# create an instance of NewAppInstanceInput from a dict
new_app_instance_input_from_dict = NewAppInstanceInput.from_dict(new_app_instance_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


