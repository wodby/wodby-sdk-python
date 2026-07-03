# ClusterSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_infrastructure_upgrade** | [**ClusterAutoInfrastructureUpgradeSettingsInput**](ClusterAutoInfrastructureUpgradeSettingsInput.md) |  | [optional] 

## Example

```python
from wodby.models.cluster_settings_input import ClusterSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterSettingsInput from a JSON string
cluster_settings_input_instance = ClusterSettingsInput.from_json(json)
# print the JSON string representation of the object
print(ClusterSettingsInput.to_json())

# convert the object into a dict
cluster_settings_input_dict = cluster_settings_input_instance.to_dict()
# create an instance of ClusterSettingsInput from a dict
cluster_settings_input_from_dict = ClusterSettingsInput.from_dict(cluster_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


