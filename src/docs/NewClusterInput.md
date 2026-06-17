# NewClusterInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** |  | 
**project_id** | **int** |  | [optional] 
**integration_id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**serverless** | **bool** |  | 
**single_node** | **bool** |  | [optional] 
**version** | **str** |  | [optional] 
**machine_type** | **str** |  | [optional] 
**min_node_count** | **int** |  | [optional] 
**max_node_count** | **int** |  | [optional] 
**node_disk_size** | **int** |  | [optional] 
**zone** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**billing_option** | **str** |  | [optional] 
**disable_monitoring** | **bool** |  | 

## Example

```python
from wodby.models.new_cluster_input import NewClusterInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewClusterInput from a JSON string
new_cluster_input_instance = NewClusterInput.from_json(json)
# print the JSON string representation of the object
print(NewClusterInput.to_json())

# convert the object into a dict
new_cluster_input_dict = new_cluster_input_instance.to_dict()
# create an instance of NewClusterInput from a dict
new_cluster_input_from_dict = NewClusterInput.from_dict(new_cluster_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


