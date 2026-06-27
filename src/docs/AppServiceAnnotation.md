# AppServiceAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**app_service_id** | **int** |  | 
**name** | **str** |  | 
**value** | **str** |  | 
**env_type** | **str** |  | [optional] 
**source** | [**AppServiceAnnotationSource**](AppServiceAnnotationSource.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from wodby.models.app_service_annotation import AppServiceAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceAnnotation from a JSON string
app_service_annotation_instance = AppServiceAnnotation.from_json(json)
# print the JSON string representation of the object
print(AppServiceAnnotation.to_json())

# convert the object into a dict
app_service_annotation_dict = app_service_annotation_instance.to_dict()
# create an instance of AppServiceAnnotation from a dict
app_service_annotation_from_dict = AppServiceAnnotation.from_dict(app_service_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


