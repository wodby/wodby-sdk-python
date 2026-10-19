# StackAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**value** | **str** |  | [optional] 
**env_type** | **str** | Limit the value to app environments of this type. | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from wodby.models.stack_annotation import StackAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of StackAnnotation from a JSON string
stack_annotation_instance = StackAnnotation.from_json(json)
# print the JSON string representation of the object
print(StackAnnotation.to_json())

# convert the object into a dict
stack_annotation_dict = stack_annotation_instance.to_dict()
# create an instance of StackAnnotation from a dict
stack_annotation_from_dict = StackAnnotation.from_dict(stack_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


