# AppDeployment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**number** | **int** |  | 
**status** | **str** |  | 
**rollback_status** | **str** |  | 
**post_deployment_status** | **str** |  | 
**skip_rollback** | **bool** |  | 
**app_instance_id** | **int** |  | 
**builds** | [**List[AppBuild]**](AppBuild.md) |  | 
**task_id** | **int** |  | [optional] 
**task** | [**Task**](Task.md) |  | [optional] 
**post_deployment_task_id** | **int** |  | [optional] 
**post_deployment_task** | [**Task**](Task.md) |  | [optional] 
**app_service_deployments** | [**List[AppServiceDeployment]**](AppServiceDeployment.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**started_at** | **datetime** |  | [optional] 
**ended_at** | **datetime** |  | [optional] 

## Example

```python
from wodby.models.app_deployment import AppDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of AppDeployment from a JSON string
app_deployment_instance = AppDeployment.from_json(json)
# print the JSON string representation of the object
print(AppDeployment.to_json())

# convert the object into a dict
app_deployment_dict = app_deployment_instance.to_dict()
# create an instance of AppDeployment from a dict
app_deployment_from_dict = AppDeployment.from_dict(app_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


