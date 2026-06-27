# AppServiceCronJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**app_service_id** | **int** |  | 
**schedule_id** | **int** |  | [optional] 
**task_id** | **int** |  | [optional] 
**title** | **str** |  | 
**command** | **str** |  | 
**status** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.app_service_cron_job import AppServiceCronJob

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceCronJob from a JSON string
app_service_cron_job_instance = AppServiceCronJob.from_json(json)
# print the JSON string representation of the object
print(AppServiceCronJob.to_json())

# convert the object into a dict
app_service_cron_job_dict = app_service_cron_job_instance.to_dict()
# create an instance of AppServiceCronJob from a dict
app_service_cron_job_from_dict = AppServiceCronJob.from_dict(app_service_cron_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


