# AppServiceDeployment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**job_name** | **str** |  | 
**status** | **str** |  | 
**app_service_id** | **int** |  | 
**app_service_build_id** | **int** |  | [optional] 
**previous_app_service_build_id** | **int** |  | [optional] 
**build_selection_kind** | **str** |  | 
**skip_post_deployment** | **bool** |  | 
**force** | **bool** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**started_at** | **datetime** |  | [optional] 
**ended_at** | **datetime** |  | [optional] 

## Example

```python
from wodby.models.app_service_deployment import AppServiceDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceDeployment from a JSON string
app_service_deployment_instance = AppServiceDeployment.from_json(json)
# print the JSON string representation of the object
print(AppServiceDeployment.to_json())

# convert the object into a dict
app_service_deployment_dict = app_service_deployment_instance.to_dict()
# create an instance of AppServiceDeployment from a dict
app_service_deployment_from_dict = AppServiceDeployment.from_dict(app_service_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


