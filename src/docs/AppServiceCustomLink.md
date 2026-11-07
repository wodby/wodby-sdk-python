# AppServiceCustomLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_service_id** | **int** |  | 
**name** | **str** |  | 
**values** | [**List[AppServiceCustomLinkValue]**](AppServiceCustomLinkValue.md) | The values the link declares, in its order. | 

## Example

```python
from wodby.models.app_service_custom_link import AppServiceCustomLink

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceCustomLink from a JSON string
app_service_custom_link_instance = AppServiceCustomLink.from_json(json)
# print the JSON string representation of the object
print(AppServiceCustomLink.to_json())

# convert the object into a dict
app_service_custom_link_dict = app_service_custom_link_instance.to_dict()
# create an instance of AppServiceCustomLink from a dict
app_service_custom_link_from_dict = AppServiceCustomLink.from_dict(app_service_custom_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


