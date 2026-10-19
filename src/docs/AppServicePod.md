# AppServicePod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**workload** | **str** |  | 
**kube_workload_name** | **str** |  | 
**node** | **str** |  | [optional] 
**phase** | **str** |  | 
**ready** | **bool** |  | 
**terminating** | **bool** |  | 
**reason** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**cpu_usage** | **float** | CPU cores in use. | [optional] 
**memory_usage** | **int** | Memory in use in bytes. | [optional] 
**cpu_request** | **float** |  | [optional] 
**memory_request** | **int** |  | [optional] 
**cpu_limit** | **float** |  | [optional] 
**memory_limit** | **int** |  | [optional] 
**containers** | [**List[AppServicePodContainer]**](AppServicePodContainer.md) |  | 

## Example

```python
from wodby.models.app_service_pod import AppServicePod

# TODO update the JSON string below
json = "{}"
# create an instance of AppServicePod from a JSON string
app_service_pod_instance = AppServicePod.from_json(json)
# print the JSON string representation of the object
print(AppServicePod.to_json())

# convert the object into a dict
app_service_pod_dict = app_service_pod_instance.to_dict()
# create an instance of AppServicePod from a dict
app_service_pod_from_dict = AppServicePod.from_dict(app_service_pod_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


