# ClusterAutoKubernetesUpgradeSettings

Automatic Kubernetes version upgrades. Kubernetes versions are 1.MINOR.PATCH, so there is no major upgrade. A newer provider build of the same version, such as 1.36.5-do.1 to 1.36.5-do.2, counts as a patch. When there is no version upgrade to start, the same policy and window apply the cluster's component updates, such as Cilium on k3s and EKS add-ons, unless includeComponentUpdates is off; an update within the component's minor counts as a patch. Always disabled for Wodby Cloud and serverless clusters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**allow_patch** | **bool** |  | 
**allow_minor** | **bool** |  | 
**minor_only_after_end_of_life** | **bool** | Holds an allowed minor upgrade until the current minor reaches upstream end of life. | 
**time_window** | [**AutomationTimeWindow**](AutomationTimeWindow.md) | When an upgrade may start. Absent means any time. | [optional] 
**include_component_updates** | **bool** | Also applies the cluster&#39;s component updates when there is no version upgrade to start, under the same policy and window. On by default. | 

## Example

```python
from wodby.models.cluster_auto_kubernetes_upgrade_settings import ClusterAutoKubernetesUpgradeSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAutoKubernetesUpgradeSettings from a JSON string
cluster_auto_kubernetes_upgrade_settings_instance = ClusterAutoKubernetesUpgradeSettings.from_json(json)
# print the JSON string representation of the object
print(ClusterAutoKubernetesUpgradeSettings.to_json())

# convert the object into a dict
cluster_auto_kubernetes_upgrade_settings_dict = cluster_auto_kubernetes_upgrade_settings_instance.to_dict()
# create an instance of ClusterAutoKubernetesUpgradeSettings from a dict
cluster_auto_kubernetes_upgrade_settings_from_dict = ClusterAutoKubernetesUpgradeSettings.from_dict(cluster_auto_kubernetes_upgrade_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


