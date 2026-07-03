# ClusterAutoInfrastructureComponentSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**version_policy** | [**ClusterAutoUpgradeVersionPolicyInput**](ClusterAutoUpgradeVersionPolicyInput.md) |  | [optional] 

## Example

```python
from wodby.models.cluster_auto_infrastructure_component_settings_input import ClusterAutoInfrastructureComponentSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAutoInfrastructureComponentSettingsInput from a JSON string
cluster_auto_infrastructure_component_settings_input_instance = ClusterAutoInfrastructureComponentSettingsInput.from_json(json)
# print the JSON string representation of the object
print(ClusterAutoInfrastructureComponentSettingsInput.to_json())

# convert the object into a dict
cluster_auto_infrastructure_component_settings_input_dict = cluster_auto_infrastructure_component_settings_input_instance.to_dict()
# create an instance of ClusterAutoInfrastructureComponentSettingsInput from a dict
cluster_auto_infrastructure_component_settings_input_from_dict = ClusterAutoInfrastructureComponentSettingsInput.from_dict(cluster_auto_infrastructure_component_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


