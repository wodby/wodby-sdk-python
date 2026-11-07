# ClusterComponentUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | cilium upgrades the Cilium release on a K3S cluster; provider_addon asks the provider to update an add-on. | 
**name** | **str** | Identifies the update within its cluster. | 
**current_version** | **str** | Absent when the update replaces a copy the provider does not manage yet. | [optional] 
**target_version** | **str** |  | 
**components** | **List[str]** | The names of the cluster components this update changes. | 
**note** | **str** | What to expect while the update runs. | [optional] 

## Example

```python
from wodby.models.cluster_component_update import ClusterComponentUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterComponentUpdate from a JSON string
cluster_component_update_instance = ClusterComponentUpdate.from_json(json)
# print the JSON string representation of the object
print(ClusterComponentUpdate.to_json())

# convert the object into a dict
cluster_component_update_dict = cluster_component_update_instance.to_dict()
# create an instance of ClusterComponentUpdate from a dict
cluster_component_update_from_dict = ClusterComponentUpdate.from_dict(cluster_component_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


