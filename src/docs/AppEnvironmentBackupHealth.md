# AppEnvironmentBackupHealth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failing_schedules_count** | **int** |  | 
**latest_failure_at** | **datetime** |  | [optional] 

## Example

```python
from wodby.models.app_environment_backup_health import AppEnvironmentBackupHealth

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironmentBackupHealth from a JSON string
app_environment_backup_health_instance = AppEnvironmentBackupHealth.from_json(json)
# print the JSON string representation of the object
print(AppEnvironmentBackupHealth.to_json())

# convert the object into a dict
app_environment_backup_health_dict = app_environment_backup_health_instance.to_dict()
# create an instance of AppEnvironmentBackupHealth from a dict
app_environment_backup_health_from_dict = AppEnvironmentBackupHealth.from_dict(app_environment_backup_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


