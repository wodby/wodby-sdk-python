# ScaleClusterInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_node_count** | **int** |  | 
**max_node_count** | **int** |  | 

## Example

```python
from wodby.models.scale_cluster_input import ScaleClusterInput

# TODO update the JSON string below
json = "{}"
# create an instance of ScaleClusterInput from a JSON string
scale_cluster_input_instance = ScaleClusterInput.from_json(json)
# print the JSON string representation of the object
print(ScaleClusterInput.to_json())

# convert the object into a dict
scale_cluster_input_dict = scale_cluster_input_instance.to_dict()
# create an instance of ScaleClusterInput from a dict
scale_cluster_input_from_dict = ScaleClusterInput.from_dict(scale_cluster_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


