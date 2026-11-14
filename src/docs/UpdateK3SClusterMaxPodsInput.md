# UpdateK3SClusterMaxPodsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_pods** | **int** | Pods each node runs at most. | 

## Example

```python
from wodby.models.update_k3_s_cluster_max_pods_input import UpdateK3SClusterMaxPodsInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateK3SClusterMaxPodsInput from a JSON string
update_k3_s_cluster_max_pods_input_instance = UpdateK3SClusterMaxPodsInput.from_json(json)
# print the JSON string representation of the object
print(UpdateK3SClusterMaxPodsInput.to_json())

# convert the object into a dict
update_k3_s_cluster_max_pods_input_dict = update_k3_s_cluster_max_pods_input_instance.to_dict()
# create an instance of UpdateK3SClusterMaxPodsInput from a dict
update_k3_s_cluster_max_pods_input_from_dict = UpdateK3SClusterMaxPodsInput.from_dict(update_k3_s_cluster_max_pods_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


