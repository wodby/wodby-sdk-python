# IntegrationProviderRevisionUpgrade


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | 
**reasons** | **List[str]** |  | 
**removed_fields** | **List[str]** |  | 
**can_drop_removed_fields** | **bool** |  | 
**current_revision** | [**ProviderRevision**](ProviderRevision.md) |  | 
**target_revision** | [**ProviderRevision**](ProviderRevision.md) |  | 

## Example

```python
from wodby.models.integration_provider_revision_upgrade import IntegrationProviderRevisionUpgrade

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationProviderRevisionUpgrade from a JSON string
integration_provider_revision_upgrade_instance = IntegrationProviderRevisionUpgrade.from_json(json)
# print the JSON string representation of the object
print(IntegrationProviderRevisionUpgrade.to_json())

# convert the object into a dict
integration_provider_revision_upgrade_dict = integration_provider_revision_upgrade_instance.to_dict()
# create an instance of IntegrationProviderRevisionUpgrade from a dict
integration_provider_revision_upgrade_from_dict = IntegrationProviderRevisionUpgrade.from_dict(integration_provider_revision_upgrade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


