# StackServiceAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**stack_service_id** | **int** |  | 
**name** | **str** |  | 
**value** | **str** |  | [optional] 
**env_type** | **str** |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from wodby.models.stack_service_annotation import StackServiceAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of StackServiceAnnotation from a JSON string
stack_service_annotation_instance = StackServiceAnnotation.from_json(json)
# print the JSON string representation of the object
print(StackServiceAnnotation.to_json())

# convert the object into a dict
stack_service_annotation_dict = stack_service_annotation_instance.to_dict()
# create an instance of StackServiceAnnotation from a dict
stack_service_annotation_from_dict = StackServiceAnnotation.from_dict(stack_service_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


