# Backup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**status** | **str** |  | 
**app_instance_id** | **int** |  | [optional] 
**app_service_id** | **int** |  | [optional] 
**database_id** | **int** |  | [optional] 
**database_db_id** | **int** |  | [optional] 
**backup_preset_id** | **int** |  | [optional] 
**manual** | **bool** |  | 
**integration_id** | **int** | Storage integration that owns the backup. Null identifies Wodby&#39;s built-in blob storage. | 
**task_id** | **int** |  | [optional] 
**size** | **int** | Final stored archive size in bytes. Null when the size has not been recorded. | [optional] 
**options** | [**List[BackupOption]**](BackupOption.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**started_at** | **datetime** |  | [optional] 
**ended_at** | **datetime** |  | [optional] 

## Example

```python
from wodby.models.backup import Backup

# TODO update the JSON string below
json = "{}"
# create an instance of Backup from a JSON string
backup_instance = Backup.from_json(json)
# print the JSON string representation of the object
print(Backup.to_json())

# convert the object into a dict
backup_dict = backup_instance.to_dict()
# create an instance of Backup from a dict
backup_from_dict = Backup.from_dict(backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


