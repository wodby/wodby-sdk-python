# Service


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**type** | **str** |  | 
**status** | **str** |  | 
**external** | **bool** |  | 
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
**settings** | [**ServiceSettings**](ServiceSettings.md) |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.service import Service

# TODO update the JSON string below
json = "{}"
# create an instance of Service from a JSON string
service_instance = Service.from_json(json)
# print the JSON string representation of the object
print(Service.to_json())

# convert the object into a dict
service_dict = service_instance.to_dict()
# create an instance of Service from a dict
service_from_dict = Service.from_dict(service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


