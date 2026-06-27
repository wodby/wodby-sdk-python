# AppServiceCronJobsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AppServiceCronJob]**](AppServiceCronJob.md) |  | 
**total_count** | **int** |  | 
**next_page** | **int** |  | [optional] 

## Example

```python
from wodby.models.app_service_cron_jobs_response import AppServiceCronJobsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceCronJobsResponse from a JSON string
app_service_cron_jobs_response_instance = AppServiceCronJobsResponse.from_json(json)
# print the JSON string representation of the object
print(AppServiceCronJobsResponse.to_json())

# convert the object into a dict
app_service_cron_jobs_response_dict = app_service_cron_jobs_response_instance.to_dict()
# create an instance of AppServiceCronJobsResponse from a dict
app_service_cron_jobs_response_from_dict = AppServiceCronJobsResponse.from_dict(app_service_cron_jobs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


