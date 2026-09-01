# UpgradeIntegrationProviderRevisionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drop_removed_fields** | **bool** | Permanently deletes fields absent from the target revision when the preview allows it. | 

## Example

```python
from wodby.models.upgrade_integration_provider_revision_input import UpgradeIntegrationProviderRevisionInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeIntegrationProviderRevisionInput from a JSON string
upgrade_integration_provider_revision_input_instance = UpgradeIntegrationProviderRevisionInput.from_json(json)
# print the JSON string representation of the object
print(UpgradeIntegrationProviderRevisionInput.to_json())

# convert the object into a dict
upgrade_integration_provider_revision_input_dict = upgrade_integration_provider_revision_input_instance.to_dict()
# create an instance of UpgradeIntegrationProviderRevisionInput from a dict
upgrade_integration_provider_revision_input_from_dict = UpgradeIntegrationProviderRevisionInput.from_dict(upgrade_integration_provider_revision_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


