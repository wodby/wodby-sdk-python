# ClusterCapabilityPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_install** | **bool** |  | 
**stack_revision_ids** | **List[int]** | Approved immutable stack revision IDs for discovery and optional installation. | 

## Example

```python
from wodby.models.cluster_capability_policy import ClusterCapabilityPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCapabilityPolicy from a JSON string
cluster_capability_policy_instance = ClusterCapabilityPolicy.from_json(json)
# print the JSON string representation of the object
print(ClusterCapabilityPolicy.to_json())

# convert the object into a dict
cluster_capability_policy_dict = cluster_capability_policy_instance.to_dict()
# create an instance of ClusterCapabilityPolicy from a dict
cluster_capability_policy_from_dict = ClusterCapabilityPolicy.from_dict(cluster_capability_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


