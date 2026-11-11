# StackSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_auto_update** | [**GitAutoUpdateSettings**](GitAutoUpdateSettings.md) |  | [optional] 
**auto_service_revision_update** | [**StackAutoServiceRevisionUpdateSettings**](StackAutoServiceRevisionUpdateSettings.md) |  | [optional] 
**auto_origin_stack_update** | [**StackAutoOriginUpdateSettings**](StackAutoOriginUpdateSettings.md) |  | [optional] 
**git_service_updates** | **str** | What an automatic update from Git, started by a push, does with existing stack services whose stack.yml reference has no version: latest moves them to the service&#39;s latest version, auto_update_settings (the default) moves them only as far as the stack&#39;s service auto update settings allow, and keep keeps their version. Manual updates move them to the latest version unless the update&#39;s serviceUpdates says otherwise. Versioned references, pinned stack services and new ones resolve the same way in every mode, and a stack service whose stack.yml configures something only a newer version has always moves to it. | [optional] 

## Example

```python
from wodby.models.stack_settings import StackSettings

# TODO update the JSON string below
json = "{}"
# create an instance of StackSettings from a JSON string
stack_settings_instance = StackSettings.from_json(json)
# print the JSON string representation of the object
print(StackSettings.to_json())

# convert the object into a dict
stack_settings_dict = stack_settings_instance.to_dict()
# create an instance of StackSettings from a dict
stack_settings_from_dict = StackSettings.from_dict(stack_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


