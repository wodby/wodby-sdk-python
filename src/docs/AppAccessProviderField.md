# AppAccessProviderField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**label** | **str** |  | 
**description** | **str** |  | 
**required** | **bool** |  | 
**radio** | **bool** |  | 
**hostname_suffix** | **bool** |  | 
**affects_hostname** | **bool** |  | 
**default_value** | **str** |  | [optional] 
**options** | [**List[AppAccessProviderOption]**](AppAccessProviderOption.md) |  | 

## Example

```python
from wodby.models.app_access_provider_field import AppAccessProviderField

# TODO update the JSON string below
json = "{}"
# create an instance of AppAccessProviderField from a JSON string
app_access_provider_field_instance = AppAccessProviderField.from_json(json)
# print the JSON string representation of the object
print(AppAccessProviderField.to_json())

# convert the object into a dict
app_access_provider_field_dict = app_access_provider_field_instance.to_dict()
# create an instance of AppAccessProviderField from a dict
app_access_provider_field_from_dict = AppAccessProviderField.from_dict(app_access_provider_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


