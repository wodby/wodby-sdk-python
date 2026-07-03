# ClusterAutoInfrastructureUpgradeSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**infra** | [**ClusterAutoInfrastructureComponentSettings**](ClusterAutoInfrastructureComponentSettings.md) |  | [optional] 
**apps** | [**ClusterAutoInfrastructureComponentSettings**](ClusterAutoInfrastructureComponentSettings.md) |  | [optional] 

## Example

```python
from wodby.models.cluster_auto_infrastructure_upgrade_settings import ClusterAutoInfrastructureUpgradeSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAutoInfrastructureUpgradeSettings from a JSON string
cluster_auto_infrastructure_upgrade_settings_instance = ClusterAutoInfrastructureUpgradeSettings.from_json(json)
# print the JSON string representation of the object
print(ClusterAutoInfrastructureUpgradeSettings.to_json())

# convert the object into a dict
cluster_auto_infrastructure_upgrade_settings_dict = cluster_auto_infrastructure_upgrade_settings_instance.to_dict()
# create an instance of ClusterAutoInfrastructureUpgradeSettings from a dict
cluster_auto_infrastructure_upgrade_settings_from_dict = ClusterAutoInfrastructureUpgradeSettings.from_dict(cluster_auto_infrastructure_upgrade_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


