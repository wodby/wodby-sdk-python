# StackSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_auto_update** | [**GitAutoUpdateSettingsInput**](GitAutoUpdateSettingsInput.md) |  | [optional] 
**auto_service_revision_update** | [**StackAutoServiceRevisionUpdateSettingsInput**](StackAutoServiceRevisionUpdateSettingsInput.md) |  | [optional] 
**auto_origin_stack_update** | [**StackAutoOriginUpdateSettingsInput**](StackAutoOriginUpdateSettingsInput.md) |  | [optional] 

## Example

```python
from wodby.models.stack_settings_input import StackSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of StackSettingsInput from a JSON string
stack_settings_input_instance = StackSettingsInput.from_json(json)
# print the JSON string representation of the object
print(StackSettingsInput.to_json())

# convert the object into a dict
stack_settings_input_dict = stack_settings_input_instance.to_dict()
# create an instance of StackSettingsInput from a dict
stack_settings_input_from_dict = StackSettingsInput.from_dict(stack_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


