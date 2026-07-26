# UpdateAppRouteInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** |  | [optional] 
**main** | **bool** |  | [optional] 
**primary** | **bool** |  | [optional] 
**path** | **str** |  | [optional] 
**path_type** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**redirect_scheme** | **str** |  | [optional] 
**redirect_host** | **str** |  | [optional] 
**redirect_path** | **str** |  | [optional] 
**redirect_status_code** | **int** |  | [optional] 

## Example

```python
from wodby.models.update_app_route_input import UpdateAppRouteInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAppRouteInput from a JSON string
update_app_route_input_instance = UpdateAppRouteInput.from_json(json)
# print the JSON string representation of the object
print(UpdateAppRouteInput.to_json())

# convert the object into a dict
update_app_route_input_dict = update_app_route_input_instance.to_dict()
# create an instance of UpdateAppRouteInput from a dict
update_app_route_input_from_dict = UpdateAppRouteInput.from_dict(update_app_route_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


