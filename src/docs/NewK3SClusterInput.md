# NewK3SClusterInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** | Optional for API-key requests; defaults to the API key&#39;s organization. | [optional] 
**project_id** | **int** |  | [optional] 
**available_to_all_projects** | **bool** | Lets every project in the organization use the new resource without a project share. Only an organization-owned resource, created without projectId, can be available to all projects. | [optional] 
**name** | **str** |  | 
**title** | **str** |  | 
**disable_monitoring** | **bool** |  | 
**auto_infrastructure_upgrade** | **bool** |  | [optional] 
**environment_policy** | [**ClusterEnvironmentPolicyInput**](ClusterEnvironmentPolicyInput.md) |  | [optional] 

## Example

```python
from wodby.models.new_k3_s_cluster_input import NewK3SClusterInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewK3SClusterInput from a JSON string
new_k3_s_cluster_input_instance = NewK3SClusterInput.from_json(json)
# print the JSON string representation of the object
print(NewK3SClusterInput.to_json())

# convert the object into a dict
new_k3_s_cluster_input_dict = new_k3_s_cluster_input_instance.to_dict()
# create an instance of NewK3SClusterInput from a dict
new_k3_s_cluster_input_from_dict = NewK3SClusterInput.from_dict(new_k3_s_cluster_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


