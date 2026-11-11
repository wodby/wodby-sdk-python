# Stack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**icon** | **str** |  | 
**status** | **str** |  | 
**outdated** | **bool** |  | 
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
**variant_of_stack_id** | **int** | Main stack this stack is a variant of, such as Drupal for a high-availability Drupal stack. Absent when the stack is not a variant, or the main stack does not exist or is not visible to you. | [optional] 
**variant_of_stack_name** | **str** |  | [optional] 
**variant_title** | **str** | Short label that tells this variant apart, such as High availability. | [optional] 
**variant_description** | **str** | When to choose this stack over the other stacks of its variant family, such as building the app from your own repository to customize it. A main stack can have one too. | [optional] 
**variant_stack_ids** | **List[int]** | Variants of this stack that you can see, ordered by title. Empty for a stack that is a variant itself. | 
**org_id** | **int** |  | 
**ownership_scope** | **str** | org when the organization owns the resource, project when one project owns it. | 
**owner_project_id** | **int** |  | [optional] 
**available_to_all_projects** | **bool** | True when every project in the organization can use the resource without a project share. | 
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


