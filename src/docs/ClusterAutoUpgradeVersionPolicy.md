# ClusterAutoUpgradeVersionPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_patch** | **bool** |  | 
**allow_minor** | **bool** |  | 
**allow_major** | **bool** |  | 

## Example

```python
from wodby.models.cluster_auto_upgrade_version_policy import ClusterAutoUpgradeVersionPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAutoUpgradeVersionPolicy from a JSON string
cluster_auto_upgrade_version_policy_instance = ClusterAutoUpgradeVersionPolicy.from_json(json)
# print the JSON string representation of the object
print(ClusterAutoUpgradeVersionPolicy.to_json())

# convert the object into a dict
cluster_auto_upgrade_version_policy_dict = cluster_auto_upgrade_version_policy_instance.to_dict()
# create an instance of ClusterAutoUpgradeVersionPolicy from a dict
cluster_auto_upgrade_version_policy_from_dict = ClusterAutoUpgradeVersionPolicy.from_dict(cluster_auto_upgrade_version_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


