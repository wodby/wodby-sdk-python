# ServiceSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_auto_update** | [**GitAutoUpdateSettingsInput**](GitAutoUpdateSettingsInput.md) |  | [optional] 
**auto_base_revision_update** | [**ServiceAutoBaseRevisionUpdateSettingsInput**](ServiceAutoBaseRevisionUpdateSettingsInput.md) |  | [optional] 

## Example

```python
from wodby.models.service_settings_input import ServiceSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSettingsInput from a JSON string
service_settings_input_instance = ServiceSettingsInput.from_json(json)
# print the JSON string representation of the object
print(ServiceSettingsInput.to_json())

# convert the object into a dict
service_settings_input_dict = service_settings_input_instance.to_dict()
# create an instance of ServiceSettingsInput from a dict
service_settings_input_from_dict = ServiceSettingsInput.from_dict(service_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


