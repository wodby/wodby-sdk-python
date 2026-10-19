# AppDeployment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**number** | **int** |  | 
**status** | **str** | Overall result, including the routing updates that follow the service rollout. | 
**rollout_status** | **str** | Progress of rolling out the selected services. It does not show whether routing has finished. | 
**rollout_ended_at** | **datetime** |  | [optional] 
**rollback_status** | **str** |  | 
**post_deployment_status** | **str** |  | 
**skip_rollback** | **bool** |  | 
**can_cancel** | **bool** |  | 
**app_instance_id** | **int** |  | 
**builds** | [**List[AppBuild]**](AppBuild.md) |  | 
**preparation_task_id** | **int** |  | [optional] 
**preparation_task** | [**Task**](Task.md) |  | [optional] 
**task_id** | **int** |  | [optional] 
**task** | [**Task**](Task.md) |  | [optional] 
**post_deployment_task_id** | **int** |  | [optional] 
**post_deployment_task** | [**Task**](Task.md) |  | [optional] 
**app_service_deployments** | [**List[AppServiceDeployment]**](AppServiceDeployment.md) |  | 
**post_deployment_scripts** | **List[str]** | Post-deployment scripts that the deployment&#39;s builds provide. | 
**skip_post_deployment_scripts** | **bool** | True when the deployment does not run the post-deployment scripts its builds provide. | 
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


