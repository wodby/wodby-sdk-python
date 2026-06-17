# TaskJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**status** | **str** |  | 
**after** | **List[str]** |  | [optional] 
**timeout** | **int** |  | 
**is_system** | **bool** |  | 
**status_title** | **str** |  | 
**steps** | [**List[TaskStep]**](TaskStep.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**started_at** | **datetime** |  | [optional] 
**ended_at** | **datetime** |  | [optional] 

## Example

```python
from wodby.models.task_job import TaskJob

# TODO update the JSON string below
json = "{}"
# create an instance of TaskJob from a JSON string
task_job_instance = TaskJob.from_json(json)
# print the JSON string representation of the object
print(TaskJob.to_json())

# convert the object into a dict
task_job_dict = task_job_instance.to_dict()
# create an instance of TaskJob from a dict
task_job_from_dict = TaskJob.from_dict(task_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


