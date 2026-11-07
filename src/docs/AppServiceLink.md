# AppServiceLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**app_service_id** | **int** |  | 
**linked_app_service_id** | **int** |  | 
**name** | **str** |  | 
**cross_app** | **bool** | The linked app service is in another app environment, of the same app or another one. | 
**target_app_instance_id** | **int** | The app environment of a linked app service in another environment; null otherwise. | [optional] 
**target_app_instance_name** | **str** |  | [optional] 
**target_app_instance_title** | **str** |  | [optional] 
**target_app_id** | **int** | The app of a linked app service in another environment; null otherwise. | [optional] 
**target_app_name** | **str** |  | [optional] 
**target_app_title** | **str** |  | [optional] 

## Example

```python
from wodby.models.app_service_link import AppServiceLink

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceLink from a JSON string
app_service_link_instance = AppServiceLink.from_json(json)
# print the JSON string representation of the object
print(AppServiceLink.to_json())

# convert the object into a dict
app_service_link_dict = app_service_link_instance.to_dict()
# create an instance of AppServiceLink from a dict
app_service_link_from_dict = AppServiceLink.from_dict(app_service_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


