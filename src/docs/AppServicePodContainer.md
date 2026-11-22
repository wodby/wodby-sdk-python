# AppServicePodContainer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**primary** | **bool** |  | 
**ready** | **bool** |  | 
**restarts** | **int** |  | 
**state** | **str** |  | 
**reason** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**exit_code** | **int** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**last_termination_reason** | **str** | Why the container&#39;s previous run ended, such as OOMKilled or Error. Null when it hasn&#39;t restarted. | [optional] 
**last_exit_code** | **int** | Exit code of the container&#39;s previous run. Null when it hasn&#39;t restarted. | [optional] 
**last_finished_at** | **datetime** | When the container&#39;s previous run ended. Null when it hasn&#39;t restarted. | [optional] 
**cpu_usage** | **float** |  | [optional] 
**memory_usage** | **int** |  | [optional] 
**cpu_request** | **float** |  | [optional] 
**memory_request** | **int** |  | [optional] 
**cpu_limit** | **float** |  | [optional] 
**memory_limit** | **int** |  | [optional] 

## Example

```python
from wodby.models.app_service_pod_container import AppServicePodContainer

# TODO update the JSON string below
json = "{}"
# create an instance of AppServicePodContainer from a JSON string
app_service_pod_container_instance = AppServicePodContainer.from_json(json)
# print the JSON string representation of the object
print(AppServicePodContainer.to_json())

# convert the object into a dict
app_service_pod_container_dict = app_service_pod_container_instance.to_dict()
# create an instance of AppServicePodContainer from a dict
app_service_pod_container_from_dict = AppServicePodContainer.from_dict(app_service_pod_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


