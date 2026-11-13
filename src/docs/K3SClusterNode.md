# K3SClusterNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**role** | **str** | server runs the k3s control plane; agent is a worker node joined with the join command. | 
**ready** | **bool** |  | 
**schedulable** | **bool** | Whether the node accepts new pods. A node being removed or upgraded doesn&#39;t. | 
**version** | **str** | The node&#39;s k3s release, such as v1.36.6+k3s1. | 
**internal_ip** | **str** | The private address the node uses for cluster traffic. | [optional] 
**external_ip** | **str** |  | [optional] 
**local_volumes** | **List[str]** | Persistent volumes stored on the node, as namespace/name of their claims. Their data stays on that server, so removing the node loses it. | 
**created_at** | **datetime** |  | 

## Example

```python
from wodby.models.k3_s_cluster_node import K3SClusterNode

# TODO update the JSON string below
json = "{}"
# create an instance of K3SClusterNode from a JSON string
k3_s_cluster_node_instance = K3SClusterNode.from_json(json)
# print the JSON string representation of the object
print(K3SClusterNode.to_json())

# convert the object into a dict
k3_s_cluster_node_dict = k3_s_cluster_node_instance.to_dict()
# create an instance of K3SClusterNode from a dict
k3_s_cluster_node_from_dict = K3SClusterNode.from_dict(k3_s_cluster_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


