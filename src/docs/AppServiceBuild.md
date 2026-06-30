# AppServiceBuild


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**status** | **str** |  | 
**image** | **str** |  | 
**image_deleted** | **bool** |  | 
**size** | **int** |  | 
**app_service_id** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.app_service_build import AppServiceBuild

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceBuild from a JSON string
app_service_build_instance = AppServiceBuild.from_json(json)
# print the JSON string representation of the object
print(AppServiceBuild.to_json())

# convert the object into a dict
app_service_build_dict = app_service_build_instance.to_dict()
# create an instance of AppServiceBuild from a dict
app_service_build_from_dict = AppServiceBuild.from_dict(app_service_build_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


