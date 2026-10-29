# AppEnvironmentPreview

Pull request metadata of an automatic preview environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** |  | 
**title** | **str** |  | 
**url** | **str** |  | 
**head_ref** | **str** |  | 
**head_sha** | **str** |  | 
**base_ref** | **str** |  | 
**author** | **str** |  | 
**draft** | **bool** |  | 
**base_app_environment_id** | **int** |  | [optional] 
**last_activity_at** | **datetime** |  | 
**closed_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from wodby.models.app_environment_preview import AppEnvironmentPreview

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironmentPreview from a JSON string
app_environment_preview_instance = AppEnvironmentPreview.from_json(json)
# print the JSON string representation of the object
print(AppEnvironmentPreview.to_json())

# convert the object into a dict
app_environment_preview_dict = app_environment_preview_instance.to_dict()
# create an instance of AppEnvironmentPreview from a dict
app_environment_preview_from_dict = AppEnvironmentPreview.from_dict(app_environment_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


