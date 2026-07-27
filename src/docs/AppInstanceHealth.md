# AppInstanceHealth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron** | [**AppInstanceCronHealth**](AppInstanceCronHealth.md) |  | 
**backups** | [**AppInstanceBackupHealth**](AppInstanceBackupHealth.md) |  | 

## Example

```python
from wodby.models.app_instance_health import AppInstanceHealth

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstanceHealth from a JSON string
app_instance_health_instance = AppInstanceHealth.from_json(json)
# print the JSON string representation of the object
print(AppInstanceHealth.to_json())

# convert the object into a dict
app_instance_health_dict = app_instance_health_instance.to_dict()
# create an instance of AppInstanceHealth from a dict
app_instance_health_from_dict = AppInstanceHealth.from_dict(app_instance_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


