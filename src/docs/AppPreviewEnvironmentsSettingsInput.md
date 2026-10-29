# AppPreviewEnvironmentsSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**base_app_environment_id** | **int** |  | [optional] 
**environment_type** | **str** |  | [optional] 
**imports** | [**List[AppPreviewImport]**](AppPreviewImport.md) |  | [optional] 
**build_drafts** | **bool** |  | [optional] 
**run_cron_jobs** | **bool** | Omitted keeps the stored value; apps that never set it do not run cron jobs in previews. | [optional] 
**max_concurrent** | **int** |  | [optional] 
**idle_ttl_days** | **int** |  | [optional] 

## Example

```python
from wodby.models.app_preview_environments_settings_input import AppPreviewEnvironmentsSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppPreviewEnvironmentsSettingsInput from a JSON string
app_preview_environments_settings_input_instance = AppPreviewEnvironmentsSettingsInput.from_json(json)
# print the JSON string representation of the object
print(AppPreviewEnvironmentsSettingsInput.to_json())

# convert the object into a dict
app_preview_environments_settings_input_dict = app_preview_environments_settings_input_instance.to_dict()
# create an instance of AppPreviewEnvironmentsSettingsInput from a dict
app_preview_environments_settings_input_from_dict = AppPreviewEnvironmentsSettingsInput.from_dict(app_preview_environments_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


