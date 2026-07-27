# ClusterMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**cluster_id** | **int** |  | 
**nodes_total** | **int** |  | 
**nodes_ready** | **int** |  | 
**cpu** | [**KubeCPUMetrics**](KubeCPUMetrics.md) |  | 
**memory** | [**KubeMemoryMetrics**](KubeMemoryMetrics.md) |  | 
**kube_cpu_cap** | [**CapacityMetricsFloat**](CapacityMetricsFloat.md) |  | 
**kube_memory_cap** | [**CapacityMetrics**](CapacityMetrics.md) |  | 
**kube_pods_cap** | [**CapacityMetrics**](CapacityMetrics.md) |  | 
**host_disk** | [**NodeDiskMetrics**](NodeDiskMetrics.md) |  | [optional] 

## Example

```python
from wodby.models.cluster_metrics import ClusterMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMetrics from a JSON string
cluster_metrics_instance = ClusterMetrics.from_json(json)
# print the JSON string representation of the object
print(ClusterMetrics.to_json())

# convert the object into a dict
cluster_metrics_dict = cluster_metrics_instance.to_dict()
# create an instance of ClusterMetrics from a dict
cluster_metrics_from_dict = ClusterMetrics.from_dict(cluster_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


