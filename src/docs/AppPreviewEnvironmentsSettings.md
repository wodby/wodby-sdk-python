# AppPreviewEnvironmentsSettings

Automatic preview environments for pull requests opened against the branch tracked by the base environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**base_app_environment_id** | **int** |  | [optional] 
**environment_type** | **str** |  | 
**imports** | [**List[AppPreviewImport]**](AppPreviewImport.md) |  | 
**build_drafts** | **bool** |  | 
**run_cron_jobs** | **bool** | Run the base environment&#39;s cron jobs in every preview. When false, the default, cron jobs are copied disabled. Previews never copy backup presets and run every service with one replica. | 
**max_concurrent** | **int** |  | 
**idle_ttl_days** | **int** |  | 

## Example

```python
from wodby.models.app_preview_environments_settings import AppPreviewEnvironmentsSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AppPreviewEnvironmentsSettings from a JSON string
app_preview_environments_settings_instance = AppPreviewEnvironmentsSettings.from_json(json)
# print the JSON string representation of the object
print(AppPreviewEnvironmentsSettings.to_json())

# convert the object into a dict
app_preview_environments_settings_dict = app_preview_environments_settings_instance.to_dict()
# create an instance of AppPreviewEnvironmentsSettings from a dict
app_preview_environments_settings_from_dict = AppPreviewEnvironmentsSettings.from_dict(app_preview_environments_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


