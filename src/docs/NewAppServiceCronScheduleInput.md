# NewAppServiceCronScheduleInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Stable cron schedule identity. When omitted or blank, the server generates a unique name. | [optional] 
**title** | **str** |  | 
**crontab** | **str** |  | 
**command** | **str** |  | 
**workload** | **str** |  | [optional] 
**disabled** | **bool** | Creates the schedule disabled. Disabled schedules do not require cron feature access. | [optional] 

## Example

```python
from wodby.models.new_app_service_cron_schedule_input import NewAppServiceCronScheduleInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewAppServiceCronScheduleInput from a JSON string
new_app_service_cron_schedule_input_instance = NewAppServiceCronScheduleInput.from_json(json)
# print the JSON string representation of the object
print(NewAppServiceCronScheduleInput.to_json())

# convert the object into a dict
new_app_service_cron_schedule_input_dict = new_app_service_cron_schedule_input_instance.to_dict()
# create an instance of NewAppServiceCronScheduleInput from a dict
new_app_service_cron_schedule_input_from_dict = NewAppServiceCronScheduleInput.from_dict(new_app_service_cron_schedule_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


