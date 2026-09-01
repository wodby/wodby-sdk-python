# NewAppEnvironmentAccessEndpointInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_service_name** | **str** | Machine name of an enabled app service from the selected stack revision. | 
**app_port_name** | **str** | Machine name of a public HTTP port from that service manifest. | 
**primary** | **bool** |  | 

## Example

```python
from wodby.models.new_app_environment_access_endpoint_input import NewAppEnvironmentAccessEndpointInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewAppEnvironmentAccessEndpointInput from a JSON string
new_app_environment_access_endpoint_input_instance = NewAppEnvironmentAccessEndpointInput.from_json(json)
# print the JSON string representation of the object
print(NewAppEnvironmentAccessEndpointInput.to_json())

# convert the object into a dict
new_app_environment_access_endpoint_input_dict = new_app_environment_access_endpoint_input_instance.to_dict()
# create an instance of NewAppEnvironmentAccessEndpointInput from a dict
new_app_environment_access_endpoint_input_from_dict = NewAppEnvironmentAccessEndpointInput.from_dict(new_app_environment_access_endpoint_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


