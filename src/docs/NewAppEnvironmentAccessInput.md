# NewAppEnvironmentAccessInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **int** |  | 
**mode** | **str** |  | 
**scope** | **str** |  | 
**settings** | [**List[AppAccessSettingInput]**](AppAccessSettingInput.md) |  | [optional] 
**host** | **str** | Required only when the selected provider uses a customer-assigned hostname. | [optional] 
**endpoints** | [**List[NewAppEnvironmentAccessEndpointInput]**](NewAppEnvironmentAccessEndpointInput.md) | HTTP endpoints selected during creation. Used only with SELECTED_ENDPOINTS scope; older clients may omit it to select the main endpoint. | [optional] 

## Example

```python
from wodby.models.new_app_environment_access_input import NewAppEnvironmentAccessInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewAppEnvironmentAccessInput from a JSON string
new_app_environment_access_input_instance = NewAppEnvironmentAccessInput.from_json(json)
# print the JSON string representation of the object
print(NewAppEnvironmentAccessInput.to_json())

# convert the object into a dict
new_app_environment_access_input_dict = new_app_environment_access_input_instance.to_dict()
# create an instance of NewAppEnvironmentAccessInput from a dict
new_app_environment_access_input_from_dict = NewAppEnvironmentAccessInput.from_dict(new_app_environment_access_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


