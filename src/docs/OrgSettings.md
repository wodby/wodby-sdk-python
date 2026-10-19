# OrgSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_image_cleanup** | [**BuildImageCleanupSettings**](BuildImageCleanupSettings.md) | Default build image retention for the organization&#39;s app environments. | [optional] 

## Example

```python
from wodby.models.org_settings import OrgSettings

# TODO update the JSON string below
json = "{}"
# create an instance of OrgSettings from a JSON string
org_settings_instance = OrgSettings.from_json(json)
# print the JSON string representation of the object
print(OrgSettings.to_json())

# convert the object into a dict
org_settings_dict = org_settings_instance.to_dict()
# create an instance of OrgSettings from a dict
org_settings_from_dict = OrgSettings.from_dict(org_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


