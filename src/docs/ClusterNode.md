# ClusterNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**ready** | **bool** |  | 
**schedulable** | **bool** | Whether the node accepts new pods. A node being drained, recycled or upgraded doesn&#39;t. | 
**version** | **str** | The node&#39;s Kubernetes version, as its kubelet reports it. | 
**machine_type** | **str** | The provider&#39;s machine type of the node, such as m6i.large, when the node reports it. | [optional] 
**zone** | **str** | The availability zone of the node, when the node reports it. | [optional] 
**gpu_node_pool** | **bool** | Whether the node belongs to the cluster&#39;s GPU node pool. | 
**internal_ip** | **str** |  | [optional] 
**external_ip** | **str** |  | [optional] 
**capacity** | [**NodeCapacity**](NodeCapacity.md) |  | 
**created_at** | **datetime** |  | 

## Example

```python
from wodby.models.cluster_node import ClusterNode

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNode from a JSON string
cluster_node_instance = ClusterNode.from_json(json)
# print the JSON string representation of the object
print(ClusterNode.to_json())

# convert the object into a dict
cluster_node_dict = cluster_node_instance.to_dict()
# create an instance of ClusterNode from a dict
cluster_node_from_dict = ClusterNode.from_dict(cluster_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


