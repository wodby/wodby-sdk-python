# AppServiceCustomization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section** | **str** | The part of the app service where the customization is: general, resources, variables, helm, annotations, settings, links, integrations, volumes or configs. | 
**name** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from wodby.models.app_service_customization import AppServiceCustomization

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceCustomization from a JSON string
app_service_customization_instance = AppServiceCustomization.from_json(json)
# print the JSON string representation of the object
print(AppServiceCustomization.to_json())

# convert the object into a dict
app_service_customization_dict = app_service_customization_instance.to_dict()
# create an instance of AppServiceCustomization from a dict
app_service_customization_from_dict = AppServiceCustomization.from_dict(app_service_customization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


