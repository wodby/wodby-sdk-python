# KubeCPUMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cores** | **int** |  | 
**load1** | **float** |  | 
**load5** | **float** |  | 
**load15** | **float** |  | 
**idle** | **float** |  | [optional] 
**io_wait** | **float** |  | [optional] 
**steal** | **float** |  | [optional] 

## Example

```python
from wodby.models.kube_cpu_metrics import KubeCPUMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of KubeCPUMetrics from a JSON string
kube_cpu_metrics_instance = KubeCPUMetrics.from_json(json)
# print the JSON string representation of the object
print(KubeCPUMetrics.to_json())

# convert the object into a dict
kube_cpu_metrics_dict = kube_cpu_metrics_instance.to_dict()
# create an instance of KubeCPUMetrics from a dict
kube_cpu_metrics_from_dict = KubeCPUMetrics.from_dict(kube_cpu_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


