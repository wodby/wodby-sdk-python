# ServiceSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_auto_update** | [**GitAutoUpdateSettings**](GitAutoUpdateSettings.md) |  | [optional] 

## Example

```python
from wodby.models.service_settings import ServiceSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSettings from a JSON string
service_settings_instance = ServiceSettings.from_json(json)
# print the JSON string representation of the object
print(ServiceSettings.to_json())

# convert the object into a dict
service_settings_dict = service_settings_instance.to_dict()
# create an instance of ServiceSettings from a dict
service_settings_from_dict = ServiceSettings.from_dict(service_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


