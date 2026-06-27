# UpdateStackServiceCronScheduleInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**crontab** | **str** |  | [optional] 
**command** | **str** |  | [optional] 
**workload** | **str** |  | [optional] 
**env_type** | **str** |  | [optional] 

## Example

```python
from wodby.models.update_stack_service_cron_schedule_input import UpdateStackServiceCronScheduleInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStackServiceCronScheduleInput from a JSON string
update_stack_service_cron_schedule_input_instance = UpdateStackServiceCronScheduleInput.from_json(json)
# print the JSON string representation of the object
print(UpdateStackServiceCronScheduleInput.to_json())

# convert the object into a dict
update_stack_service_cron_schedule_input_dict = update_stack_service_cron_schedule_input_instance.to_dict()
# create an instance of UpdateStackServiceCronScheduleInput from a dict
update_stack_service_cron_schedule_input_from_dict = UpdateStackServiceCronScheduleInput.from_dict(update_stack_service_cron_schedule_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


