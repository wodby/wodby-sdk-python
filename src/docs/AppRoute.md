# AppRoute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**host** | **str** |  | 
**path** | **str** |  | 
**path_type** | **str** |  | 
**action** | **str** |  | 
**redirect_scheme** | **str** |  | [optional] 
**redirect_host** | **str** |  | [optional] 
**redirect_path** | **str** |  | [optional] 
**redirect_status_code** | **int** |  | [optional] 
**status** | **str** |  | 
**disabled** | **bool** |  | 
**main** | **bool** |  | 
**primary** | **bool** |  | 
**private** | **bool** |  | 
**app_instance_id** | **int** |  | 
**app_service_id** | **int** |  | 
**port_id** | **int** |  | 
**cert** | [**Cert**](Cert.md) |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**last_synced_at** | **datetime** |  | [optional] 

## Example

```python
from wodby.models.app_route import AppRoute

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoute from a JSON string
app_route_instance = AppRoute.from_json(json)
# print the JSON string representation of the object
print(AppRoute.to_json())

# convert the object into a dict
app_route_dict = app_route_instance.to_dict()
# create an instance of AppRoute from a dict
app_route_from_dict = AppRoute.from_dict(app_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


