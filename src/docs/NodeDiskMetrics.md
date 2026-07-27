# NodeDiskMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** |  | 
**fs_type** | **str** |  | 
**size** | **int** |  | 
**free** | **int** |  | 
**i_nodes** | **int** |  | 
**i_nodes_free** | **int** |  | 

## Example

```python
from wodby.models.node_disk_metrics import NodeDiskMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of NodeDiskMetrics from a JSON string
node_disk_metrics_instance = NodeDiskMetrics.from_json(json)
# print the JSON string representation of the object
print(NodeDiskMetrics.to_json())

# convert the object into a dict
node_disk_metrics_dict = node_disk_metrics_instance.to_dict()
# create an instance of NodeDiskMetrics from a dict
node_disk_metrics_from_dict = NodeDiskMetrics.from_dict(node_disk_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


