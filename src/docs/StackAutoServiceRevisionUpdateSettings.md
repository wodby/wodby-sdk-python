# StackAutoServiceRevisionUpdateSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**policy** | [**StackAutoUpdatePolicy**](StackAutoUpdatePolicy.md) |  | [optional] 

## Example

```python
from wodby.models.stack_auto_service_revision_update_settings import StackAutoServiceRevisionUpdateSettings

# TODO update the JSON string below
json = "{}"
# create an instance of StackAutoServiceRevisionUpdateSettings from a JSON string
stack_auto_service_revision_update_settings_instance = StackAutoServiceRevisionUpdateSettings.from_json(json)
# print the JSON string representation of the object
print(StackAutoServiceRevisionUpdateSettings.to_json())

# convert the object into a dict
stack_auto_service_revision_update_settings_dict = stack_auto_service_revision_update_settings_instance.to_dict()
# create an instance of StackAutoServiceRevisionUpdateSettings from a dict
stack_auto_service_revision_update_settings_from_dict = StackAutoServiceRevisionUpdateSettings.from_dict(stack_auto_service_revision_update_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


