# AppServiceLinkInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linked_app_service_id** | **int** |  | [optional] 

## Example

```python
from wodby.models.app_service_link_input import AppServiceLinkInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceLinkInput from a JSON string
app_service_link_input_instance = AppServiceLinkInput.from_json(json)
# print the JSON string representation of the object
print(AppServiceLinkInput.to_json())

# convert the object into a dict
app_service_link_input_dict = app_service_link_input_instance.to_dict()
# create an instance of AppServiceLinkInput from a dict
app_service_link_input_from_dict = AppServiceLinkInput.from_dict(app_service_link_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


