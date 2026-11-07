# AppServiceCustomLinkValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**secret** | **bool** |  | 
**has_value** | **bool** |  | 
**value** | **str** | The value; null for a secret value. | 

## Example

```python
from wodby.models.app_service_custom_link_value import AppServiceCustomLinkValue

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceCustomLinkValue from a JSON string
app_service_custom_link_value_instance = AppServiceCustomLinkValue.from_json(json)
# print the JSON string representation of the object
print(AppServiceCustomLinkValue.to_json())

# convert the object into a dict
app_service_custom_link_value_dict = app_service_custom_link_value_instance.to_dict()
# create an instance of AppServiceCustomLinkValue from a dict
app_service_custom_link_value_from_dict = AppServiceCustomLinkValue.from_dict(app_service_custom_link_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


