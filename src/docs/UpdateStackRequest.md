# UpdateStackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique stack machine name within the organization. | 
**title** | **str** | Human-readable stack title. | 

## Example

```python
from wodby.models.update_stack_request import UpdateStackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStackRequest from a JSON string
update_stack_request_instance = UpdateStackRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateStackRequest.to_json())

# convert the object into a dict
update_stack_request_dict = update_stack_request_instance.to_dict()
# create an instance of UpdateStackRequest from a dict
update_stack_request_from_dict = UpdateStackRequest.from_dict(update_stack_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


