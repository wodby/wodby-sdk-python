# ClusterNodePoolInput

An optional GPU node pool. Only machine types that report GPUs are accepted, and the provider must support GPU node pools.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine_type** | **str** |  | 
**min_node_count** | **int** | Zero lets the pool scale down to no nodes where the provider supports it. | 
**max_node_count** | **int** |  | 
**node_disk_size** | **int** | Node disk size in GB. Required when the provider&#39;s node disk size is configurable. | [optional] 

## Example

```python
from wodby.models.cluster_node_pool_input import ClusterNodePoolInput

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNodePoolInput from a JSON string
cluster_node_pool_input_instance = ClusterNodePoolInput.from_json(json)
# print the JSON string representation of the object
print(ClusterNodePoolInput.to_json())

# convert the object into a dict
cluster_node_pool_input_dict = cluster_node_pool_input_instance.to_dict()
# create an instance of ClusterNodePoolInput from a dict
cluster_node_pool_input_from_dict = ClusterNodePoolInput.from_dict(cluster_node_pool_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


