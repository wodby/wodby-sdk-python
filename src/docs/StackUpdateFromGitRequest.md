# StackUpdateFromGitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_ref** | **str** |  | 
**git_ref_type** | **str** |  | 
**service_updates** | **str** | What this update does with existing stack services whose stack.yml reference has no version, instead of the stack&#39;s gitServiceUpdates setting: latest, auto_update_settings or keep. | [optional] 

## Example

```python
from wodby.models.stack_update_from_git_request import StackUpdateFromGitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StackUpdateFromGitRequest from a JSON string
stack_update_from_git_request_instance = StackUpdateFromGitRequest.from_json(json)
# print the JSON string representation of the object
print(StackUpdateFromGitRequest.to_json())

# convert the object into a dict
stack_update_from_git_request_dict = stack_update_from_git_request_instance.to_dict()
# create an instance of StackUpdateFromGitRequest from a dict
stack_update_from_git_request_from_dict = StackUpdateFromGitRequest.from_dict(stack_update_from_git_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


