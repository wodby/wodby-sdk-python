# ClusterNodePool

An optional node pool of the cluster, such as the GPU node pool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine_type** | **str** |  | 
**min_node_count** | **int** |  | 
**max_node_count** | **int** |  | 
**node_disk_size** | **int** |  | [optional] 

## Example

```python
from wodby.models.cluster_node_pool import ClusterNodePool

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNodePool from a JSON string
cluster_node_pool_instance = ClusterNodePool.from_json(json)
# print the JSON string representation of the object
print(ClusterNodePool.to_json())

# convert the object into a dict
cluster_node_pool_dict = cluster_node_pool_instance.to_dict()
# create an instance of ClusterNodePool from a dict
cluster_node_pool_from_dict = ClusterNodePool.from_dict(cluster_node_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


