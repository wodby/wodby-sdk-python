# ClusterAutoInfrastructureUpgradeSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**infra** | [**ClusterAutoInfrastructureComponentSettingsInput**](ClusterAutoInfrastructureComponentSettingsInput.md) |  | [optional] 
**apps** | [**ClusterAutoInfrastructureComponentSettingsInput**](ClusterAutoInfrastructureComponentSettingsInput.md) |  | [optional] 

## Example

```python
from wodby.models.cluster_auto_infrastructure_upgrade_settings_input import ClusterAutoInfrastructureUpgradeSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAutoInfrastructureUpgradeSettingsInput from a JSON string
cluster_auto_infrastructure_upgrade_settings_input_instance = ClusterAutoInfrastructureUpgradeSettingsInput.from_json(json)
# print the JSON string representation of the object
print(ClusterAutoInfrastructureUpgradeSettingsInput.to_json())

# convert the object into a dict
cluster_auto_infrastructure_upgrade_settings_input_dict = cluster_auto_infrastructure_upgrade_settings_input_instance.to_dict()
# create an instance of ClusterAutoInfrastructureUpgradeSettingsInput from a dict
cluster_auto_infrastructure_upgrade_settings_input_from_dict = ClusterAutoInfrastructureUpgradeSettingsInput.from_dict(cluster_auto_infrastructure_upgrade_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


