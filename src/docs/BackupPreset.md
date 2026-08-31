# BackupPreset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**app_instance_id** | **int** |  | [optional] 
**app_service_id** | **int** |  | [optional] 
**database_id** | **int** |  | [optional] 
**database_db_id** | **int** |  | [optional] 
**org_id** | **int** |  | [optional] 
**env_id** | **int** |  | [optional] 
**backup_name** | **str** |  | [optional] 
**integration_id** | **int** |  | 
**bucket** | **str** |  | 
**storage_class** | **str** |  | [optional] 
**options** | [**List[BackupOption]**](BackupOption.md) |  | 
**override** | **bool** |  | 
**auto** | **bool** |  | 
**disabled** | **bool** |  | 
**crontab** | **str** |  | [optional] 
**time_window** | [**AutomationTimeWindow**](AutomationTimeWindow.md) |  | [optional] 
**duration** | **int** |  | [optional] 
**next_run_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.backup_preset import BackupPreset

# TODO update the JSON string below
json = "{}"
# create an instance of BackupPreset from a JSON string
backup_preset_instance = BackupPreset.from_json(json)
# print the JSON string representation of the object
print(BackupPreset.to_json())

# convert the object into a dict
backup_preset_dict = backup_preset_instance.to_dict()
# create an instance of BackupPreset from a dict
backup_preset_from_dict = BackupPreset.from_dict(backup_preset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


