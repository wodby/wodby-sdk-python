# ClusterAutoKubernetesUpgradeSettingsInput

Omitted fields keep their current values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**allow_patch** | **bool** |  | [optional] 
**allow_minor** | **bool** |  | [optional] 
**minor_only_after_end_of_life** | **bool** |  | [optional] 
**include_component_updates** | **bool** |  | [optional] 
**time_window** | [**AutomationTimeWindowInput**](AutomationTimeWindowInput.md) | A window with enabled false lets upgrades start at any time. | [optional] 

## Example

```python
from wodby.models.cluster_auto_kubernetes_upgrade_settings_input import ClusterAutoKubernetesUpgradeSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAutoKubernetesUpgradeSettingsInput from a JSON string
cluster_auto_kubernetes_upgrade_settings_input_instance = ClusterAutoKubernetesUpgradeSettingsInput.from_json(json)
# print the JSON string representation of the object
print(ClusterAutoKubernetesUpgradeSettingsInput.to_json())

# convert the object into a dict
cluster_auto_kubernetes_upgrade_settings_input_dict = cluster_auto_kubernetes_upgrade_settings_input_instance.to_dict()
# create an instance of ClusterAutoKubernetesUpgradeSettingsInput from a dict
cluster_auto_kubernetes_upgrade_settings_input_from_dict = ClusterAutoKubernetesUpgradeSettingsInput.from_dict(cluster_auto_kubernetes_upgrade_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


