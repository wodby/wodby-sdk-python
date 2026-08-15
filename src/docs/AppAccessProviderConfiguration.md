# AppAccessProviderConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | 
**endpoint_host_mode** | **str** |  | 
**fields** | [**List[AppAccessProviderField]**](AppAccessProviderField.md) |  | 

## Example

```python
from wodby.models.app_access_provider_configuration import AppAccessProviderConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AppAccessProviderConfiguration from a JSON string
app_access_provider_configuration_instance = AppAccessProviderConfiguration.from_json(json)
# print the JSON string representation of the object
print(AppAccessProviderConfiguration.to_json())

# convert the object into a dict
app_access_provider_configuration_dict = app_access_provider_configuration_instance.to_dict()
# create an instance of AppAccessProviderConfiguration from a dict
app_access_provider_configuration_from_dict = AppAccessProviderConfiguration.from_dict(app_access_provider_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


