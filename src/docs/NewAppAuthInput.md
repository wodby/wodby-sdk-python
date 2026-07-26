# NewAppAuthInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_instance_id** | **int** |  | 
**app_service_id** | **int** | Optional service scope. Required together with appRouteId for route scope. | [optional] 
**app_route_id** | **int** | Optional route scope. Requires appServiceId and must belong to that service. | [optional] 
**login** | **str** |  | 
**password** | **str** |  | 
**realm** | **str** |  | 

## Example

```python
from wodby.models.new_app_auth_input import NewAppAuthInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewAppAuthInput from a JSON string
new_app_auth_input_instance = NewAppAuthInput.from_json(json)
# print the JSON string representation of the object
print(NewAppAuthInput.to_json())

# convert the object into a dict
new_app_auth_input_dict = new_app_auth_input_instance.to_dict()
# create an instance of NewAppAuthInput from a dict
new_app_auth_input_from_dict = NewAppAuthInput.from_dict(new_app_auth_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


