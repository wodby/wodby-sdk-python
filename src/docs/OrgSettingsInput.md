# OrgSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_image_cleanup** | [**BuildImageCleanupSettingsInput**](BuildImageCleanupSettingsInput.md) |  | 

## Example

```python
from wodby.models.org_settings_input import OrgSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of OrgSettingsInput from a JSON string
org_settings_input_instance = OrgSettingsInput.from_json(json)
# print the JSON string representation of the object
print(OrgSettingsInput.to_json())

# convert the object into a dict
org_settings_input_dict = org_settings_input_instance.to_dict()
# create an instance of OrgSettingsInput from a dict
org_settings_input_from_dict = OrgSettingsInput.from_dict(org_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


