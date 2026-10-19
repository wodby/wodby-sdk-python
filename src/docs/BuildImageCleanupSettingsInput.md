# BuildImageCleanupSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retention** | **str** |  | 

## Example

```python
from wodby.models.build_image_cleanup_settings_input import BuildImageCleanupSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of BuildImageCleanupSettingsInput from a JSON string
build_image_cleanup_settings_input_instance = BuildImageCleanupSettingsInput.from_json(json)
# print the JSON string representation of the object
print(BuildImageCleanupSettingsInput.to_json())

# convert the object into a dict
build_image_cleanup_settings_input_dict = build_image_cleanup_settings_input_instance.to_dict()
# create an instance of BuildImageCleanupSettingsInput from a dict
build_image_cleanup_settings_input_from_dict = BuildImageCleanupSettingsInput.from_dict(build_image_cleanup_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


