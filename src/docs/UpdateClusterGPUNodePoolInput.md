# UpdateClusterGPUNodePoolInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_node_pool** | [**ClusterNodePoolInput**](ClusterNodePoolInput.md) |  | 

## Example

```python
from wodby.models.update_cluster_gpu_node_pool_input import UpdateClusterGPUNodePoolInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClusterGPUNodePoolInput from a JSON string
update_cluster_gpu_node_pool_input_instance = UpdateClusterGPUNodePoolInput.from_json(json)
# print the JSON string representation of the object
print(UpdateClusterGPUNodePoolInput.to_json())

# convert the object into a dict
update_cluster_gpu_node_pool_input_dict = update_cluster_gpu_node_pool_input_instance.to_dict()
# create an instance of UpdateClusterGPUNodePoolInput from a dict
update_cluster_gpu_node_pool_input_from_dict = UpdateClusterGPUNodePoolInput.from_dict(update_cluster_gpu_node_pool_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


