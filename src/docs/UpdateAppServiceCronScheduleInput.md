# UpdateAppServiceCronScheduleInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**crontab** | **str** |  | [optional] 
**command** | **str** |  | [optional] 
**workload** | **str** |  | [optional] 

## Example

```python
from wodby.models.update_app_service_cron_schedule_input import UpdateAppServiceCronScheduleInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAppServiceCronScheduleInput from a JSON string
update_app_service_cron_schedule_input_instance = UpdateAppServiceCronScheduleInput.from_json(json)
# print the JSON string representation of the object
print(UpdateAppServiceCronScheduleInput.to_json())

# convert the object into a dict
update_app_service_cron_schedule_input_dict = update_app_service_cron_schedule_input_instance.to_dict()
# create an instance of UpdateAppServiceCronScheduleInput from a dict
update_app_service_cron_schedule_input_from_dict = UpdateAppServiceCronScheduleInput.from_dict(update_app_service_cron_schedule_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


