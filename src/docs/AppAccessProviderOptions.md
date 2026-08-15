# AppAccessProviderOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | 
**modes** | **List[str]** |  | 
**scopes** | **List[str]** |  | 
**endpoint_host_mode** | **str** |  | 
**fields** | [**List[AppAccessProviderField]**](AppAccessProviderField.md) |  | 
**configurations** | [**List[AppAccessProviderConfiguration]**](AppAccessProviderConfiguration.md) |  | 

## Example

```python
from wodby.models.app_access_provider_options import AppAccessProviderOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AppAccessProviderOptions from a JSON string
app_access_provider_options_instance = AppAccessProviderOptions.from_json(json)
# print the JSON string representation of the object
print(AppAccessProviderOptions.to_json())

# convert the object into a dict
app_access_provider_options_dict = app_access_provider_options_instance.to_dict()
# create an instance of AppAccessProviderOptions from a dict
app_access_provider_options_from_dict = AppAccessProviderOptions.from_dict(app_access_provider_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


