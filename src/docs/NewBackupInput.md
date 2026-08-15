# NewBackupInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_service_id** | **int** |  | [optional] 
**database_db_id** | **int** |  | [optional] 
**backup_name** | **str** |  | [optional] 
**integration_id** | **int** | Use 0 for Wodby Blob Storage. | 
**bucket** | **str** | Must be empty for Wodby Blob Storage. | 
**storage_class** | **str** |  | [optional] 

## Example

```python
from wodby.models.new_backup_input import NewBackupInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewBackupInput from a JSON string
new_backup_input_instance = NewBackupInput.from_json(json)
# print the JSON string representation of the object
print(NewBackupInput.to_json())

# convert the object into a dict
new_backup_input_dict = new_backup_input_instance.to_dict()
# create an instance of NewBackupInput from a dict
new_backup_input_from_dict = NewBackupInput.from_dict(new_backup_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


