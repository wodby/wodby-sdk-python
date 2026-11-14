# AppServiceDeploymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_service_id** | **int** |  | 
**app_service_build_id** | **int** | Build image to deploy for this service: the &#x60;id&#x60; of an item in an app build&#39;s &#x60;appServiceBuilds&#x60; that belongs to this service, not the app build &#x60;id&#x60;. A derivative service may name its parent service&#39;s build. Use &#x60;0&#x60; to start a new build. Required for services with a build source. To deploy every image of an app build, use &#x60;POST /app-builds/{id}/deploy&#x60; instead. | [optional] 
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


