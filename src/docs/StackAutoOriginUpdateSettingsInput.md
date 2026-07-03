# StackAutoOriginUpdateSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**version_policy** | [**StackAutoOriginUpdateVersionPolicyInput**](StackAutoOriginUpdateVersionPolicyInput.md) |  | [optional] 
**sync_options** | [**StackSyncOptionsInput**](StackSyncOptionsInput.md) |  | [optional] 

## Example

```python
from wodby.models.stack_auto_origin_update_settings_input import StackAutoOriginUpdateSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of StackAutoOriginUpdateSettingsInput from a JSON string
stack_auto_origin_update_settings_input_instance = StackAutoOriginUpdateSettingsInput.from_json(json)
# print the JSON string representation of the object
print(StackAutoOriginUpdateSettingsInput.to_json())

# convert the object into a dict
stack_auto_origin_update_settings_input_dict = stack_auto_origin_update_settings_input_instance.to_dict()
# create an instance of StackAutoOriginUpdateSettingsInput from a dict
stack_auto_origin_update_settings_input_from_dict = StackAutoOriginUpdateSettingsInput.from_dict(stack_auto_origin_update_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


