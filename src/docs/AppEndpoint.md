# AppEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**app_service_id** | **int** |  | 
**app_environment_id** | **int** |  | 
**primary** | **bool** |  | 
**route_ids** | **List[int]** |  | 
**port_ids** | **List[int]** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.app_endpoint import AppEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of AppEndpoint from a JSON string
app_endpoint_instance = AppEndpoint.from_json(json)
# print the JSON string representation of the object
print(AppEndpoint.to_json())

# convert the object into a dict
app_endpoint_dict = app_endpoint_instance.to_dict()
# create an instance of AppEndpoint from a dict
app_endpoint_from_dict = AppEndpoint.from_dict(app_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


