# StackAutoOriginUpdateSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**version_policy** | [**StackAutoOriginUpdateVersionPolicy**](StackAutoOriginUpdateVersionPolicy.md) |  | [optional] 
**sync_options** | [**StackSyncOptions**](StackSyncOptions.md) |  | [optional] 

## Example

```python
from wodby.models.stack_auto_origin_update_settings import StackAutoOriginUpdateSettings

# TODO update the JSON string below
json = "{}"
# create an instance of StackAutoOriginUpdateSettings from a JSON string
stack_auto_origin_update_settings_instance = StackAutoOriginUpdateSettings.from_json(json)
# print the JSON string representation of the object
print(StackAutoOriginUpdateSettings.to_json())

# convert the object into a dict
stack_auto_origin_update_settings_dict = stack_auto_origin_update_settings_instance.to_dict()
# create an instance of StackAutoOriginUpdateSettings from a dict
stack_auto_origin_update_settings_from_dict = StackAutoOriginUpdateSettings.from_dict(stack_auto_origin_update_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


