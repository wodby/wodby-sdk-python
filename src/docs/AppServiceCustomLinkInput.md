# AppServiceCustomLinkInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[AppServiceCustomLinkInputValuesInner]**](AppServiceCustomLinkInputValuesInner.md) |  | 

## Example

```python
from wodby.models.app_service_custom_link_input import AppServiceCustomLinkInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceCustomLinkInput from a JSON string
app_service_custom_link_input_instance = AppServiceCustomLinkInput.from_json(json)
# print the JSON string representation of the object
print(AppServiceCustomLinkInput.to_json())

# convert the object into a dict
app_service_custom_link_input_dict = app_service_custom_link_input_instance.to_dict()
# create an instance of AppServiceCustomLinkInput from a dict
app_service_custom_link_input_from_dict = AppServiceCustomLinkInput.from_dict(app_service_custom_link_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


