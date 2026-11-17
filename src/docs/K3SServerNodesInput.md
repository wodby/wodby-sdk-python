# K3SServerNodesInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | **List[str]** | Node names from GET /cluster-k3s-nodes/{id}. Empty for the default nodes. | [optional] 

## Example

```python
from wodby.models.k3_s_server_nodes_input import K3SServerNodesInput

# TODO update the JSON string below
json = "{}"
# create an instance of K3SServerNodesInput from a JSON string
k3_s_server_nodes_input_instance = K3SServerNodesInput.from_json(json)
# print the JSON string representation of the object
print(K3SServerNodesInput.to_json())

# convert the object into a dict
k3_s_server_nodes_input_dict = k3_s_server_nodes_input_instance.to_dict()
# create an instance of K3SServerNodesInput from a dict
k3_s_server_nodes_input_from_dict = K3SServerNodesInput.from_dict(k3_s_server_nodes_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


