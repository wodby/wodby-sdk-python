# KubeMemoryMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**available** | **int** |  | 

## Example

```python
from wodby.models.kube_memory_metrics import KubeMemoryMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of KubeMemoryMetrics from a JSON string
kube_memory_metrics_instance = KubeMemoryMetrics.from_json(json)
# print the JSON string representation of the object
print(KubeMemoryMetrics.to_json())

# convert the object into a dict
kube_memory_metrics_dict = kube_memory_metrics_instance.to_dict()
# create an instance of KubeMemoryMetrics from a dict
kube_memory_metrics_from_dict = KubeMemoryMetrics.from_dict(kube_memory_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


