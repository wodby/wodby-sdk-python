# StackServiceCronSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**stack_service_id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**crontab** | **str** |  | 
**command** | **str** |  | 
**workload** | **str** |  | [optional] 
**disabled** | **bool** |  | 
**env_type** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.stack_service_cron_schedule import StackServiceCronSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of StackServiceCronSchedule from a JSON string
stack_service_cron_schedule_instance = StackServiceCronSchedule.from_json(json)
# print the JSON string representation of the object
print(StackServiceCronSchedule.to_json())

# convert the object into a dict
stack_service_cron_schedule_dict = stack_service_cron_schedule_instance.to_dict()
# create an instance of StackServiceCronSchedule from a dict
stack_service_cron_schedule_from_dict = StackServiceCronSchedule.from_dict(stack_service_cron_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


