# Task


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**status** | **str** |  | 
**progress** | **int** |  | 
**silent** | **bool** |  | 
**system** | **bool** |  | 
**user_id** | **int** |  | 
**user** | [**User**](User.md) |  | [optional] 
**org_id** | **int** |  | [optional] 
**project_ids** | **List[int]** |  | [optional] 
**app_id** | **int** |  | [optional] 
**app_instance_id** | **int** |  | [optional] 
**cluster_id** | **int** |  | [optional] 
**integration_id** | **int** |  | [optional] 
**service_id** | **int** |  | [optional] 
**stack_id** | **int** |  | [optional] 
**provider_id** | **int** |  | [optional] 
**origin_task_id** | **int** |  | [optional] 
**spawned_task_ids** | **List[int]** |  | [optional] 
**repeated_task_id** | **int** |  | [optional] 
**jobs** | [**List[TaskJob]**](TaskJob.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**started_at** | **datetime** |  | [optional] 
**ended_at** | **datetime** |  | [optional] 

## Example

```python
from wodby.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print(Task.to_json())

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_from_dict = Task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


