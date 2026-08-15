# NewBackupPresetInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_instance_id** | **int** |  | [optional] 
**app_service_id** | **int** |  | [optional] 
**database_id** | **int** |  | [optional] 
**database_db_id** | **int** |  | [optional] 
**org_id** | **int** | Optional for API-key requests; defaults to the API key&#39;s organization when no more specific target is provided. | [optional] 
**env_id** | **int** |  | [optional] 
**backup_name** | **str** |  | [optional] 
**integration_id** | **int** | Use 0 for Wodby Blob Storage. Free subscriptions may create only an automatic preset that is disabled. | 
**bucket** | **str** | Must be empty for Wodby Blob Storage. | 
**storage_class** | **str** |  | [optional] 
**disabled** | **bool** |  | 
**override** | **bool** |  | 
**auto** | **bool** |  | [optional] 
**crontab** | **str** |  | [optional] 
**time_window** | [**AutomationTimeWindowInput**](AutomationTimeWindowInput.md) |  | [optional] 
**duration** | **int** |  | [optional] 

## Example

```python
from wodby.models.new_backup_preset_input import NewBackupPresetInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewBackupPresetInput from a JSON string
new_backup_preset_input_instance = NewBackupPresetInput.from_json(json)
# print the JSON string representation of the object
print(NewBackupPresetInput.to_json())

# convert the object into a dict
new_backup_preset_input_dict = new_backup_preset_input_instance.to_dict()
# create an instance of NewBackupPresetInput from a dict
new_backup_preset_input_from_dict = NewBackupPresetInput.from_dict(new_backup_preset_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


