# ProviderSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_auto_update** | [**GitAutoUpdateSettingsInput**](GitAutoUpdateSettingsInput.md) |  | 

## Example

```python
from wodby.models.provider_settings_input import ProviderSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderSettingsInput from a JSON string
provider_settings_input_instance = ProviderSettingsInput.from_json(json)
# print the JSON string representation of the object
print(ProviderSettingsInput.to_json())

# convert the object into a dict
provider_settings_input_dict = provider_settings_input_instance.to_dict()
# create an instance of ProviderSettingsInput from a dict
provider_settings_input_from_dict = ProviderSettingsInput.from_dict(provider_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


