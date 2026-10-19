# BuildImageCleanupSettings

How long images of unused builds are kept in the Wodby container registry before they are voided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retention** | **str** | Age after which images of unused builds are voided automatically. never disables the cleanup. | 

## Example

```python
from wodby.models.build_image_cleanup_settings import BuildImageCleanupSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BuildImageCleanupSettings from a JSON string
build_image_cleanup_settings_instance = BuildImageCleanupSettings.from_json(json)
# print the JSON string representation of the object
print(BuildImageCleanupSettings.to_json())

# convert the object into a dict
build_image_cleanup_settings_dict = build_image_cleanup_settings_instance.to_dict()
# create an instance of BuildImageCleanupSettings from a dict
build_image_cleanup_settings_from_dict = BuildImageCleanupSettings.from_dict(build_image_cleanup_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


