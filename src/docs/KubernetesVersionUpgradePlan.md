# KubernetesVersionUpgradePlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_version** | **str** |  | 
**provider_version** | **str** |  | 
**provider** | **str** |  | 
**supported** | **bool** |  | 
**targets** | [**List[KubernetesVersionUpgradeTarget]**](KubernetesVersionUpgradeTarget.md) |  | 
**blockers** | **List[str]** |  | 
**warnings** | **List[str]** |  | 
**observed_at** | **datetime** |  | 

## Example

```python
from wodby.models.kubernetes_version_upgrade_plan import KubernetesVersionUpgradePlan

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesVersionUpgradePlan from a JSON string
kubernetes_version_upgrade_plan_instance = KubernetesVersionUpgradePlan.from_json(json)
# print the JSON string representation of the object
print(KubernetesVersionUpgradePlan.to_json())

# convert the object into a dict
kubernetes_version_upgrade_plan_dict = kubernetes_version_upgrade_plan_instance.to_dict()
# create an instance of KubernetesVersionUpgradePlan from a dict
kubernetes_version_upgrade_plan_from_dict = KubernetesVersionUpgradePlan.from_dict(kubernetes_version_upgrade_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


