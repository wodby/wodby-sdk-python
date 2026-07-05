# CopyStackSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_service_revision_update** | [**StackAutoServiceRevisionUpdateSettingsInput**](StackAutoServiceRevisionUpdateSettingsInput.md) |  | [optional] 
**auto_origin_stack_update** | [**StackAutoOriginUpdateSettingsInput**](StackAutoOriginUpdateSettingsInput.md) |  | [optional] 

## Example

```python
from wodby.models.copy_stack_settings_input import CopyStackSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of CopyStackSettingsInput from a JSON string
copy_stack_settings_input_instance = CopyStackSettingsInput.from_json(json)
# print the JSON string representation of the object
print(CopyStackSettingsInput.to_json())

# convert the object into a dict
copy_stack_settings_input_dict = copy_stack_settings_input_instance.to_dict()
# create an instance of CopyStackSettingsInput from a dict
copy_stack_settings_input_from_dict = CopyStackSettingsInput.from_dict(copy_stack_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


