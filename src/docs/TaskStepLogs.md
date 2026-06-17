# TaskStepLogs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stream_id** | **int** |  | [optional] 
**lines** | [**List[LogLine]**](LogLine.md) |  | 

## Example

```python
from wodby.models.task_step_logs import TaskStepLogs

# TODO update the JSON string below
json = "{}"
# create an instance of TaskStepLogs from a JSON string
task_step_logs_instance = TaskStepLogs.from_json(json)
# print the JSON string representation of the object
print(TaskStepLogs.to_json())

# convert the object into a dict
task_step_logs_dict = task_step_logs_instance.to_dict()
# create an instance of TaskStepLogs from a dict
task_step_logs_from_dict = TaskStepLogs.from_dict(task_step_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


