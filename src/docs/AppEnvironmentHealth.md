# AppEnvironmentHealth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron** | [**AppEnvironmentCronHealth**](AppEnvironmentCronHealth.md) |  | 
**backups** | [**AppEnvironmentBackupHealth**](AppEnvironmentBackupHealth.md) |  | 

## Example

```python
from wodby.models.app_environment_health import AppEnvironmentHealth

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironmentHealth from a JSON string
app_environment_health_instance = AppEnvironmentHealth.from_json(json)
# print the JSON string representation of the object
print(AppEnvironmentHealth.to_json())

# convert the object into a dict
app_environment_health_dict = app_environment_health_instance.to_dict()
# create an instance of AppEnvironmentHealth from a dict
app_environment_health_from_dict = AppEnvironmentHealth.from_dict(app_environment_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


