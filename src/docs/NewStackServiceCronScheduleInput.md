# NewStackServiceCronScheduleInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | 
**crontab** | **str** |  | 
**command** | **str** |  | 
**workload** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**env_type** | **str** |  | [optional] 

## Example

```python
from wodby.models.new_stack_service_cron_schedule_input import NewStackServiceCronScheduleInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewStackServiceCronScheduleInput from a JSON string
new_stack_service_cron_schedule_input_instance = NewStackServiceCronScheduleInput.from_json(json)
# print the JSON string representation of the object
print(NewStackServiceCronScheduleInput.to_json())

# convert the object into a dict
new_stack_service_cron_schedule_input_dict = new_stack_service_cron_schedule_input_instance.to_dict()
# create an instance of NewStackServiceCronScheduleInput from a dict
new_stack_service_cron_schedule_input_from_dict = NewStackServiceCronScheduleInput.from_dict(new_stack_service_cron_schedule_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


