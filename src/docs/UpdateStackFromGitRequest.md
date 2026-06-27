# UpdateStackFromGitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_ref** | **str** |  | 
**git_ref_type** | **str** |  | 

## Example

```python
from wodby.models.update_stack_from_git_request import UpdateStackFromGitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStackFromGitRequest from a JSON string
update_stack_from_git_request_instance = UpdateStackFromGitRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateStackFromGitRequest.to_json())

# convert the object into a dict
update_stack_from_git_request_dict = update_stack_from_git_request_instance.to_dict()
# create an instance of UpdateStackFromGitRequest from a dict
update_stack_from_git_request_from_dict = UpdateStackFromGitRequest.from_dict(update_stack_from_git_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


