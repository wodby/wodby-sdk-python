# AppAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**app_environment_id** | **int** |  | 
**app_service_id** | **int** |  | [optional] 
**app_route_id** | **int** |  | [optional] 
**name** | **str** |  | 
**value** | **str** |  | 
**type** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.app_annotation import AppAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of AppAnnotation from a JSON string
app_annotation_instance = AppAnnotation.from_json(json)
# print the JSON string representation of the object
print(AppAnnotation.to_json())

# convert the object into a dict
app_annotation_dict = app_annotation_instance.to_dict()
# create an instance of AppAnnotation from a dict
app_annotation_from_dict = AppAnnotation.from_dict(app_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


