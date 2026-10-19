# UpdateAppAnnotationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_service_id** | **int** |  | [optional] 
**app_route_id** | **int** |  | [optional] 
**name** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from wodby.models.update_app_annotation_input import UpdateAppAnnotationInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAppAnnotationInput from a JSON string
update_app_annotation_input_instance = UpdateAppAnnotationInput.from_json(json)
# print the JSON string representation of the object
print(UpdateAppAnnotationInput.to_json())

# convert the object into a dict
update_app_annotation_input_dict = update_app_annotation_input_instance.to_dict()
# create an instance of UpdateAppAnnotationInput from a dict
update_app_annotation_input_from_dict = UpdateAppAnnotationInput.from_dict(update_app_annotation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


