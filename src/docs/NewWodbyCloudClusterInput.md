# NewWodbyCloudClusterInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** | Optional for API-key requests; defaults to the API key&#39;s organization. | [optional] 
**project_id** | **int** |  | [optional] 
**available_to_all_projects** | **bool** | Lets every project in the organization use the new resource without a project share. Only an organization-owned resource, created without projectId, can be available to all projects. | [optional] 
**demo** | **bool** | Create a free demo cluster with limited resources. | 
**single_node** | **bool** |  | [optional] 
**region** | **str** |  | [optional] 
**machine_type** | **str** | Machine type name from GET /wodby-cloud/machine-types. | [optional] 
**min_node_count** | **int** |  | [optional] 
**max_node_count** | **int** |  | [optional] 
**environment_policy** | [**ClusterEnvironmentPolicyInput**](ClusterEnvironmentPolicyInput.md) |  | [optional] 

## Example

```python
from wodby.models.new_wodby_cloud_cluster_input import NewWodbyCloudClusterInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewWodbyCloudClusterInput from a JSON string
new_wodby_cloud_cluster_input_instance = NewWodbyCloudClusterInput.from_json(json)
# print the JSON string representation of the object
print(NewWodbyCloudClusterInput.to_json())

# convert the object into a dict
new_wodby_cloud_cluster_input_dict = new_wodby_cloud_cluster_input_instance.to_dict()
# create an instance of NewWodbyCloudClusterInput from a dict
new_wodby_cloud_cluster_input_from_dict = NewWodbyCloudClusterInput.from_dict(new_wodby_cloud_cluster_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


