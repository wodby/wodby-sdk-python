# NewAppInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** | Optional for API-key requests; defaults to the API key&#39;s organization. | [optional] 
**name** | **str** |  | 
**title** | **str** | Defaults to name when omitted. | [optional] 
**instance_name** | **str** |  | 
**instance_title** | **str** | Defaults to instanceName when omitted. | [optional] 
**domain** | **str** | Defaults to instanceName.name.orgDomain when omitted. | [optional] 
**project_id** | **int** |  | [optional] 
**stack_rev_id** | **int** |  | 
**services** | [**List[NewAppServiceInput]**](NewAppServiceInput.md) | Defaults to the stack revision&#39;s service defaults when omitted. | [optional] 
**cluster_id** | **int** |  | [optional] 
**env_id** | **int** |  | 
**ci_integration_id** | **int** |  | [optional] 
**registry_integration_id** | **int** |  | [optional] 

## Example

```python
from wodby.models.new_app_input import NewAppInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewAppInput from a JSON string
new_app_input_instance = NewAppInput.from_json(json)
# print the JSON string representation of the object
print(NewAppInput.to_json())

# convert the object into a dict
new_app_input_dict = new_app_input_instance.to_dict()
# create an instance of NewAppInput from a dict
new_app_input_from_dict = NewAppInput.from_dict(new_app_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


