# AppServiceAnnotationSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_service** | **bool** |  | 
**from_stack** | **bool** |  | 
**from_wodby** | **bool** |  | 

## Example

```python
from wodby.models.app_service_annotation_source import AppServiceAnnotationSource

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceAnnotationSource from a JSON string
app_service_annotation_source_instance = AppServiceAnnotationSource.from_json(json)
# print the JSON string representation of the object
print(AppServiceAnnotationSource.to_json())

# convert the object into a dict
app_service_annotation_source_dict = app_service_annotation_source_instance.to_dict()
# create an instance of AppServiceAnnotationSource from a dict
app_service_annotation_source_from_dict = AppServiceAnnotationSource.from_dict(app_service_annotation_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


