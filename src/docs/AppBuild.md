# AppBuild


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**number** | **int** |  | 
**status** | **str** |  | 
**app_instance_id** | **int** |  | 
**app_service_id** | **int** |  | 
**task_id** | **int** |  | [optional] 
**task** | [**Task**](Task.md) |  | [optional] 
**app_service_builds** | [**List[AppServiceBuild]**](AppServiceBuild.md) |  | 
**git_ref_type** | **str** |  | 
**git_ref** | **str** |  | 
**commit_hash** | **str** |  | 
**commit_message** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**started_at** | **datetime** |  | [optional] 
**ended_at** | **datetime** |  | [optional] 

## Example

```python
from wodby.models.app_build import AppBuild

# TODO update the JSON string below
json = "{}"
# create an instance of AppBuild from a JSON string
app_build_instance = AppBuild.from_json(json)
# print the JSON string representation of the object
print(AppBuild.to_json())

# convert the object into a dict
app_build_dict = app_build_instance.to_dict()
# create an instance of AppBuild from a dict
app_build_from_dict = AppBuild.from_dict(app_build_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


