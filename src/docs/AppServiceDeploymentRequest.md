# AppServiceDeploymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_service_id** | **int** |  | 
**app_service_build_id** | **int** |  | [optional] 
**skip_post_deployment** | **bool** |  | [optional] 
**force** | **bool** |  | 

## Example

```python
from wodby.models.app_service_deployment_request import AppServiceDeploymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceDeploymentRequest from a JSON string
app_service_deployment_request_instance = AppServiceDeploymentRequest.from_json(json)
# print the JSON string representation of the object
print(AppServiceDeploymentRequest.to_json())

# convert the object into a dict
app_service_deployment_request_dict = app_service_deployment_request_instance.to_dict()
# create an instance of AppServiceDeploymentRequest from a dict
app_service_deployment_request_from_dict = AppServiceDeploymentRequest.from_dict(app_service_deployment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


