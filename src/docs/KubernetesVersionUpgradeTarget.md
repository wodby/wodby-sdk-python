# KubernetesVersionUpgradeTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**title** | **str** |  | 
**kind** | **str** |  | 
**preview** | **bool** |  | 

## Example

```python
from wodby.models.kubernetes_version_upgrade_target import KubernetesVersionUpgradeTarget

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesVersionUpgradeTarget from a JSON string
kubernetes_version_upgrade_target_instance = KubernetesVersionUpgradeTarget.from_json(json)
# print the JSON string representation of the object
print(KubernetesVersionUpgradeTarget.to_json())

# convert the object into a dict
kubernetes_version_upgrade_target_dict = kubernetes_version_upgrade_target_instance.to_dict()
# create an instance of KubernetesVersionUpgradeTarget from a dict
kubernetes_version_upgrade_target_from_dict = KubernetesVersionUpgradeTarget.from_dict(kubernetes_version_upgrade_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


