# NewManagedClusterInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**demo** | **bool** |  | 
**single_node** | **bool** |  | [optional] 
**region** | **str** |  | [optional] 
**machine_type** | **str** |  | [optional] 
**min_node_count** | **int** |  | [optional] 
**max_node_count** | **int** |  | [optional] 

## Example

```python
from wodby.models.new_managed_cluster_input import NewManagedClusterInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewManagedClusterInput from a JSON string
new_managed_cluster_input_instance = NewManagedClusterInput.from_json(json)
# print the JSON string representation of the object
print(NewManagedClusterInput.to_json())

# convert the object into a dict
new_managed_cluster_input_dict = new_managed_cluster_input_instance.to_dict()
# create an instance of NewManagedClusterInput from a dict
new_managed_cluster_input_from_dict = NewManagedClusterInput.from_dict(new_managed_cluster_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


