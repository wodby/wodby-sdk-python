# ProviderManifestUpdateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manifest_yaml** | **str** | Complete versioned variable provider manifest YAML. | 

## Example

```python
from wodby.models.provider_manifest_update_input import ProviderManifestUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderManifestUpdateInput from a JSON string
provider_manifest_update_input_instance = ProviderManifestUpdateInput.from_json(json)
# print the JSON string representation of the object
print(ProviderManifestUpdateInput.to_json())

# convert the object into a dict
provider_manifest_update_input_dict = provider_manifest_update_input_instance.to_dict()
# create an instance of ProviderManifestUpdateInput from a dict
provider_manifest_update_input_from_dict = ProviderManifestUpdateInput.from_dict(provider_manifest_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


