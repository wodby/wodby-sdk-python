# NewAnnotationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from wodby.models.new_annotation_input import NewAnnotationInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewAnnotationInput from a JSON string
new_annotation_input_instance = NewAnnotationInput.from_json(json)
# print the JSON string representation of the object
print(NewAnnotationInput.to_json())

# convert the object into a dict
new_annotation_input_dict = new_annotation_input_instance.to_dict()
# create an instance of NewAnnotationInput from a dict
new_annotation_input_from_dict = NewAnnotationInput.from_dict(new_annotation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


