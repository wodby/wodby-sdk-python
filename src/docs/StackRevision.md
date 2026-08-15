# StackRevision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**icon** | **str** |  | 
**number** | **int** |  | 
**draft** | **bool** |  | 
**version** | **str** |  | 
**stack_id** | **int** |  | 
**manifest** | **str** |  | 
**link_issues** | [**List[StackRevisionLinkIssue]**](StackRevisionLinkIssue.md) |  | 
**created_at** | **datetime** |  | 

## Example

```python
from wodby.models.stack_revision import StackRevision

# TODO update the JSON string below
json = "{}"
# create an instance of StackRevision from a JSON string
stack_revision_instance = StackRevision.from_json(json)
# print the JSON string representation of the object
print(StackRevision.to_json())

# convert the object into a dict
stack_revision_dict = stack_revision_instance.to_dict()
# create an instance of StackRevision from a dict
stack_revision_from_dict = StackRevision.from_dict(stack_revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


