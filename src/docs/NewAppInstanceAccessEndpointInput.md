# NewAppInstanceAccessEndpointInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_service_name** | **str** | Machine name of an enabled app service from the selected stack revision. | 
**app_port_name** | **str** | Machine name of a public HTTP port from that service manifest. | 
**primary** | **bool** |  | 

## Example

```python
from wodby.models.new_app_instance_access_endpoint_input import NewAppInstanceAccessEndpointInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewAppInstanceAccessEndpointInput from a JSON string
new_app_instance_access_endpoint_input_instance = NewAppInstanceAccessEndpointInput.from_json(json)
# print the JSON string representation of the object
print(NewAppInstanceAccessEndpointInput.to_json())

# convert the object into a dict
new_app_instance_access_endpoint_input_dict = new_app_instance_access_endpoint_input_instance.to_dict()
# create an instance of NewAppInstanceAccessEndpointInput from a dict
new_app_instance_access_endpoint_input_from_dict = NewAppInstanceAccessEndpointInput.from_dict(new_app_instance_access_endpoint_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


