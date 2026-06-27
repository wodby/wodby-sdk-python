# NewStackServiceAnnotationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 
**env_type** | **str** |  | [optional] 

## Example

```python
from wodby.models.new_stack_service_annotation_input import NewStackServiceAnnotationInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewStackServiceAnnotationInput from a JSON string
new_stack_service_annotation_input_instance = NewStackServiceAnnotationInput.from_json(json)
# print the JSON string representation of the object
print(NewStackServiceAnnotationInput.to_json())

# convert the object into a dict
new_stack_service_annotation_input_dict = new_stack_service_annotation_input_instance.to_dict()
# create an instance of NewStackServiceAnnotationInput from a dict
new_stack_service_annotation_input_from_dict = NewStackServiceAnnotationInput.from_dict(new_stack_service_annotation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


