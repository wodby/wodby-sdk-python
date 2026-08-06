# ClusterAutoInfrastructureComponentSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**version_policy** | [**ClusterAutoUpgradeVersionPolicy**](ClusterAutoUpgradeVersionPolicy.md) |  | [optional] 
**time_window** | [**AutomationTimeWindow**](AutomationTimeWindow.md) |  | [optional] 

## Example

```python
from wodby.models.cluster_auto_infrastructure_component_settings import ClusterAutoInfrastructureComponentSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAutoInfrastructureComponentSettings from a JSON string
cluster_auto_infrastructure_component_settings_instance = ClusterAutoInfrastructureComponentSettings.from_json(json)
# print the JSON string representation of the object
print(ClusterAutoInfrastructureComponentSettings.to_json())

# convert the object into a dict
cluster_auto_infrastructure_component_settings_dict = cluster_auto_infrastructure_component_settings_instance.to_dict()
# create an instance of ClusterAutoInfrastructureComponentSettings from a dict
cluster_auto_infrastructure_component_settings_from_dict = ClusterAutoInfrastructureComponentSettings.from_dict(cluster_auto_infrastructure_component_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


