# AppPreviewImport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_service_name** | **str** |  | 
**import_name** | **str** |  | 
**backup_name** | **str** |  | 

## Example

```python
from wodby.models.app_preview_import import AppPreviewImport

# TODO update the JSON string below
json = "{}"
# create an instance of AppPreviewImport from a JSON string
app_preview_import_instance = AppPreviewImport.from_json(json)
# print the JSON string representation of the object
print(AppPreviewImport.to_json())

# convert the object into a dict
app_preview_import_dict = app_preview_import_instance.to_dict()
# create an instance of AppPreviewImport from a dict
app_preview_import_from_dict = AppPreviewImport.from_dict(app_preview_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


