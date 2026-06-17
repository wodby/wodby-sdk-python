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
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

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


