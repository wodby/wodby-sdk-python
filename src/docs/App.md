# App


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**status** | **str** |  | 
**cluster_app** | **bool** |  | 
**org_id** | **int** |  | 
**ownership_scope** | **str** |  | 
**owner_project_id** | **int** |  | [optional] 
**settings** | [**AppSettings**](AppSettings.md) |  | [optional] 
**creatable_environment_types** | **List[str]** | Environment types the caller can create app environments of. Returned by getApp and getAppByName only. | [optional] 
**previews_available** | **bool** | Whether pull request preview environments can work for this app: one of its environments has an enabled service connected to a branch of its own Git repository. Returned by getApp and getAppByName only. | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.app import App

# TODO update the JSON string below
json = "{}"
# create an instance of App from a JSON string
app_instance = App.from_json(json)
# print the JSON string representation of the object
print(App.to_json())

# convert the object into a dict
app_dict = app_instance.to_dict()
# create an instance of App from a dict
app_from_dict = App.from_dict(app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


