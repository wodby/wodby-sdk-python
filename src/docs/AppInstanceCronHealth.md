# AppInstanceCronHealth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failing_schedules_count** | **int** |  | 
**latest_failure_at** | **datetime** |  | [optional] 

## Example

```python
from wodby.models.app_instance_cron_health import AppInstanceCronHealth

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstanceCronHealth from a JSON string
app_instance_cron_health_instance = AppInstanceCronHealth.from_json(json)
# print the JSON string representation of the object
print(AppInstanceCronHealth.to_json())

# convert the object into a dict
app_instance_cron_health_dict = app_instance_cron_health_instance.to_dict()
# create an instance of AppInstanceCronHealth from a dict
app_instance_cron_health_from_dict = AppInstanceCronHealth.from_dict(app_instance_cron_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


