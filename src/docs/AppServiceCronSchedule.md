# AppServiceCronSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**app_service_id** | **int** |  | 
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
from wodby.models.app_service_cron_schedule import AppServiceCronSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceCronSchedule from a JSON string
app_service_cron_schedule_instance = AppServiceCronSchedule.from_json(json)
# print the JSON string representation of the object
print(AppServiceCronSchedule.to_json())

# convert the object into a dict
app_service_cron_schedule_dict = app_service_cron_schedule_instance.to_dict()
# create an instance of AppServiceCronSchedule from a dict
app_service_cron_schedule_from_dict = AppServiceCronSchedule.from_dict(app_service_cron_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


