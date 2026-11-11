# ClusterSecurityAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory** | **str** | The advisory, such as CVE-2026-98432. | 
**title** | **str** |  | 
**state** | **str** | mitigated or not_mitigated for a K3S cluster, by the protections Wodby keeps on its server. fixed or not_fixed for a managed cluster, by the node images its provider ships. | 
**action** | **str** | The operation that fixes or mitigates the advisory. Absent when nothing is needed, or when the provider has no fixed node image yet. | [optional] 
**message** | **str** | Why the cluster is in this state and what to do about it. | 

## Example

```python
from wodby.models.cluster_security_advisory import ClusterSecurityAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterSecurityAdvisory from a JSON string
cluster_security_advisory_instance = ClusterSecurityAdvisory.from_json(json)
# print the JSON string representation of the object
print(ClusterSecurityAdvisory.to_json())

# convert the object into a dict
cluster_security_advisory_dict = cluster_security_advisory_instance.to_dict()
# create an instance of ClusterSecurityAdvisory from a dict
cluster_security_advisory_from_dict = ClusterSecurityAdvisory.from_dict(cluster_security_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


