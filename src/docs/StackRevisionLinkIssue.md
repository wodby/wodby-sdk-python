# StackRevisionLinkIssue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**stack_service_id** | **int** |  | 
**stack_service_name** | **str** |  | 
**stack_service_title** | **str** |  | 
**link_name** | **str** |  | [optional] 
**target_stack_service_id** | **int** |  | [optional] 
**target_stack_service_name** | **str** |  | [optional] 
**target_stack_service_title** | **str** |  | [optional] 
**message** | **str** |  | 

## Example

```python
from wodby.models.stack_revision_link_issue import StackRevisionLinkIssue

# TODO update the JSON string below
json = "{}"
# create an instance of StackRevisionLinkIssue from a JSON string
stack_revision_link_issue_instance = StackRevisionLinkIssue.from_json(json)
# print the JSON string representation of the object
print(StackRevisionLinkIssue.to_json())

# convert the object into a dict
stack_revision_link_issue_dict = stack_revision_link_issue_instance.to_dict()
# create an instance of StackRevisionLinkIssue from a dict
stack_revision_link_issue_from_dict = StackRevisionLinkIssue.from_dict(stack_revision_link_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


