# AppAccessProviderOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**label** | **str** |  | 
**flatten_hostname_prefix** | **bool** |  | 
**warning_title** | **str** |  | [optional] 
**warning** | **str** |  | [optional] 
**warning_url** | **str** |  | [optional] 

## Example

```python
from wodby.models.app_access_provider_option import AppAccessProviderOption

# TODO update the JSON string below
json = "{}"
# create an instance of AppAccessProviderOption from a JSON string
app_access_provider_option_instance = AppAccessProviderOption.from_json(json)
# print the JSON string representation of the object
print(AppAccessProviderOption.to_json())

# convert the object into a dict
app_access_provider_option_dict = app_access_provider_option_instance.to_dict()
# create an instance of AppAccessProviderOption from a dict
app_access_provider_option_from_dict = AppAccessProviderOption.from_dict(app_access_provider_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


