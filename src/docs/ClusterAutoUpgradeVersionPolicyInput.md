# ClusterAutoUpgradeVersionPolicyInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_patch** | **bool** |  | [optional] 
**allow_minor** | **bool** |  | [optional] 
**allow_major** | **bool** |  | [optional] 

## Example

```python
from wodby.models.cluster_auto_upgrade_version_policy_input import ClusterAutoUpgradeVersionPolicyInput

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAutoUpgradeVersionPolicyInput from a JSON string
cluster_auto_upgrade_version_policy_input_instance = ClusterAutoUpgradeVersionPolicyInput.from_json(json)
# print the JSON string representation of the object
print(ClusterAutoUpgradeVersionPolicyInput.to_json())

# convert the object into a dict
cluster_auto_upgrade_version_policy_input_dict = cluster_auto_upgrade_version_policy_input_instance.to_dict()
# create an instance of ClusterAutoUpgradeVersionPolicyInput from a dict
cluster_auto_upgrade_version_policy_input_from_dict = ClusterAutoUpgradeVersionPolicyInput.from_dict(cluster_auto_upgrade_version_policy_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


