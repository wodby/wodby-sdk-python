# UpdateBackupPresetInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **int** |  | 
**bucket** | **str** |  | 
**storage_class** | **str** |  | [optional] 
**disabled** | **bool** |  | 
**override** | **bool** |  | 
**auto** | **bool** |  | 
**crontab** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 

## Example

```python
from wodby.models.update_backup_preset_input import UpdateBackupPresetInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBackupPresetInput from a JSON string
update_backup_preset_input_instance = UpdateBackupPresetInput.from_json(json)
# print the JSON string representation of the object
print(UpdateBackupPresetInput.to_json())

# convert the object into a dict
update_backup_preset_input_dict = update_backup_preset_input_instance.to_dict()
# create an instance of UpdateBackupPresetInput from a dict
update_backup_preset_input_from_dict = UpdateBackupPresetInput.from_dict(update_backup_preset_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


