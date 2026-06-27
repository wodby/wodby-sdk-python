# StackServiceLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**stack_service_id** | **int** |  | 
**linked_stack_service_id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from wodby.models.stack_service_link import StackServiceLink

# TODO update the JSON string below
json = "{}"
# create an instance of StackServiceLink from a JSON string
stack_service_link_instance = StackServiceLink.from_json(json)
# print the JSON string representation of the object
print(StackServiceLink.to_json())

# convert the object into a dict
stack_service_link_dict = stack_service_link_instance.to_dict()
# create an instance of StackServiceLink from a dict
stack_service_link_from_dict = StackServiceLink.from_dict(stack_service_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


