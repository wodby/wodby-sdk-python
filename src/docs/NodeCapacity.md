# NodeCapacity

What a node's machine provides, as the node reports it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **float** | CPU cores. | 
**memory** | **int** | Memory in bytes. | 
**disk** | **int** | The size of the node&#39;s root disk in bytes, when the node reports it. | [optional] 
**gpus** | **int** | GPUs the node offers to pods. 0 without GPUs, and until the node&#39;s GPU driver reports them. | 

## Example

```python
from wodby.models.node_capacity import NodeCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of NodeCapacity from a JSON string
node_capacity_instance = NodeCapacity.from_json(json)
# print the JSON string representation of the object
print(NodeCapacity.to_json())

# convert the object into a dict
node_capacity_dict = node_capacity_instance.to_dict()
# create an instance of NodeCapacity from a dict
node_capacity_from_dict = NodeCapacity.from_dict(node_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


