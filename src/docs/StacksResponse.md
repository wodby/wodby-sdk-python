# StacksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Stack]**](Stack.md) |  | 
**total_count** | **int** |  | 
**next_page** | **int** |  | [optional] 

## Example

```python
from wodby.models.stacks_response import StacksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StacksResponse from a JSON string
stacks_response_instance = StacksResponse.from_json(json)
# print the JSON string representation of the object
print(StacksResponse.to_json())

# convert the object into a dict
stacks_response_dict = stacks_response_instance.to_dict()
# create an instance of StacksResponse from a dict
stacks_response_from_dict = StacksResponse.from_dict(stacks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


