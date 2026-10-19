# NewAppAnnotationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_environment_id** | **int** |  | 
**app_service_id** | **int** | Limit the annotation to one service&#39;s ingress. | [optional] 
**app_route_id** | **int** | Limit the annotation to one route&#39;s ingress. | [optional] 
**name** | **str** |  | 
**value** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from wodby.models.new_app_annotation_input import NewAppAnnotationInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewAppAnnotationInput from a JSON string
new_app_annotation_input_instance = NewAppAnnotationInput.from_json(json)
# print the JSON string representation of the object
print(NewAppAnnotationInput.to_json())

# convert the object into a dict
new_app_annotation_input_dict = new_app_annotation_input_instance.to_dict()
# create an instance of NewAppAnnotationInput from a dict
new_app_annotation_input_from_dict = NewAppAnnotationInput.from_dict(new_app_annotation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


