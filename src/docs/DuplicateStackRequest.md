# DuplicateStackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** | Optional for API-key requests; defaults to the API key&#39;s organization. | [optional] 
**project_id** | **int** |  | [optional] 
**source_rev_id** | **int** | Optional immutable source stack revision to duplicate. It must belong to the stack in the request path. | [optional] 
**settings** | [**CopyStackSettingsInput**](CopyStackSettingsInput.md) |  | [optional] 

## Example

```python
from wodby.models.duplicate_stack_request import DuplicateStackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateStackRequest from a JSON string
duplicate_stack_request_instance = DuplicateStackRequest.from_json(json)
# print the JSON string representation of the object
print(DuplicateStackRequest.to_json())

# convert the object into a dict
duplicate_stack_request_dict = duplicate_stack_request_instance.to_dict()
# create an instance of DuplicateStackRequest from a dict
duplicate_stack_request_from_dict = DuplicateStackRequest.from_dict(duplicate_stack_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


