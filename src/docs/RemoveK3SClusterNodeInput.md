# RemoveK3SClusterNodeInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_name** | **str** |  | 
**force** | **bool** | Remove the node even though it stores persistent volumes, which loses their data. | [optional] 

## Example

```python
from wodby.models.remove_k3_s_cluster_node_input import RemoveK3SClusterNodeInput

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveK3SClusterNodeInput from a JSON string
remove_k3_s_cluster_node_input_instance = RemoveK3SClusterNodeInput.from_json(json)
# print the JSON string representation of the object
print(RemoveK3SClusterNodeInput.to_json())

# convert the object into a dict
remove_k3_s_cluster_node_input_dict = remove_k3_s_cluster_node_input_instance.to_dict()
# create an instance of RemoveK3SClusterNodeInput from a dict
remove_k3_s_cluster_node_input_from_dict = RemoveK3SClusterNodeInput.from_dict(remove_k3_s_cluster_node_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


