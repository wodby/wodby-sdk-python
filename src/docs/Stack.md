# Stack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**icon** | **str** |  | 
**status** | **str** |  | 
**public** | **bool** |  | 
**rev_id** | **int** |  | 
**draft_rev_id** | **int** |  | [optional] 
**latest_rev_number** | **int** |  | 
**git_repo_id** | **int** |  | [optional] 
**git_repo_remote_id** | **str** |  | [optional] 
**git_repo_ref** | **str** |  | [optional] 
**git_repo_ref_type** | **str** |  | [optional] 
**origin_stack_rev_id** | **int** |  | [optional] 
**origin_stack_rev_stack_id** | **int** |  | [optional] 
**origin_stack_rev_name** | **str** |  | [optional] 
**origin_stack_rev_number** | **int** |  | [optional] 
**origin_stack_rev_version** | **str** |  | [optional] 
**origin_stack_rev_created_at** | **datetime** |  | [optional] 
**org_id** | **int** |  | 
**settings** | [**StackSettings**](StackSettings.md) |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.stack import Stack

# TODO update the JSON string below
json = "{}"
# create an instance of Stack from a JSON string
stack_instance = Stack.from_json(json)
# print the JSON string representation of the object
print(Stack.to_json())

# convert the object into a dict
stack_dict = stack_instance.to_dict()
# create an instance of Stack from a dict
stack_from_dict = Stack.from_dict(stack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


