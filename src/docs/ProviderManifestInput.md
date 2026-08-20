# ProviderManifestInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** | Optional for API-key requests; defaults to the API key&#39;s organization. | [optional] 
**project_id** | **int** |  | [optional] 
**manifest_yaml** | **str** | Complete variable provider manifest YAML. | 

## Example

```python
from wodby.models.provider_manifest_input import ProviderManifestInput

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderManifestInput from a JSON string
provider_manifest_input_instance = ProviderManifestInput.from_json(json)
# print the JSON string representation of the object
print(ProviderManifestInput.to_json())

# convert the object into a dict
provider_manifest_input_dict = provider_manifest_input_instance.to_dict()
# create an instance of ProviderManifestInput from a dict
provider_manifest_input_from_dict = ProviderManifestInput.from_dict(provider_manifest_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


