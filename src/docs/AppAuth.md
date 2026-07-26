# AppAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**app_instance_id** | **int** |  | 
**app_service_id** | **int** |  | [optional] 
**app_route_id** | **int** |  | [optional] 
**login** | **str** |  | 
**realm** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.app_auth import AppAuth

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuth from a JSON string
app_auth_instance = AppAuth.from_json(json)
# print the JSON string representation of the object
print(AppAuth.to_json())

# convert the object into a dict
app_auth_dict = app_auth_instance.to_dict()
# create an instance of AppAuth from a dict
app_auth_from_dict = AppAuth.from_dict(app_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


