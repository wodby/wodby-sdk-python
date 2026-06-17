# NewAppRouteInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_service_id** | **int** |  | 
**main** | **bool** |  | 
**primary** | **bool** |  | 
**port** | **int** |  | 
**host** | **str** |  | 
**path** | **str** |  | [optional] 
**path_type** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**redirect_scheme** | **str** |  | [optional] 
**redirect_host** | **str** |  | [optional] 
**redirect_path** | **str** |  | [optional] 
**redirect_status_code** | **int** |  | [optional] 
**letsencrypt** | **bool** |  | [optional] 
**auth_login** | **str** |  | [optional] 
**auth_password** | **str** |  | [optional] 
**auth_id** | **int** |  | [optional] 
**options** | [**List[AppEndpointOptionInput]**](AppEndpointOptionInput.md) |  | [optional] 

## Example

```python
from wodby.models.new_app_route_input import NewAppRouteInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewAppRouteInput from a JSON string
new_app_route_input_instance = NewAppRouteInput.from_json(json)
# print the JSON string representation of the object
print(NewAppRouteInput.to_json())

# convert the object into a dict
new_app_route_input_dict = new_app_route_input_instance.to_dict()
# create an instance of NewAppRouteInput from a dict
new_app_route_input_from_dict = NewAppRouteInput.from_dict(new_app_route_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


