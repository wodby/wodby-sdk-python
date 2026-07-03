# StackAutoServiceRevisionUpdateSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**policy** | [**StackAutoUpdatePolicyInput**](StackAutoUpdatePolicyInput.md) |  | [optional] 

## Example

```python
from wodby.models.stack_auto_service_revision_update_settings_input import StackAutoServiceRevisionUpdateSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of StackAutoServiceRevisionUpdateSettingsInput from a JSON string
stack_auto_service_revision_update_settings_input_instance = StackAutoServiceRevisionUpdateSettingsInput.from_json(json)
# print the JSON string representation of the object
print(StackAutoServiceRevisionUpdateSettingsInput.to_json())

# convert the object into a dict
stack_auto_service_revision_update_settings_input_dict = stack_auto_service_revision_update_settings_input_instance.to_dict()
# create an instance of StackAutoServiceRevisionUpdateSettingsInput from a dict
stack_auto_service_revision_update_settings_input_from_dict = StackAutoServiceRevisionUpdateSettingsInput.from_dict(stack_auto_service_revision_update_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


