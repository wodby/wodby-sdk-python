# NewAppServiceInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**disabled** | **bool** |  | 
**version** | **str** |  | [optional] 
**build_source** | [**BuildSourceInput**](BuildSourceInput.md) |  | [optional] 
**imports** | [**List[ImportInput]**](ImportInput.md) |  | [optional] 
**volumes** | [**List[VolumeSizeInput]**](VolumeSizeInput.md) |  | [optional] 
**integrations** | [**List[AppServiceIntegrationInput]**](AppServiceIntegrationInput.md) |  | [optional] 
**settings** | [**List[AppServiceSettingInput]**](AppServiceSettingInput.md) |  | [optional] 
**database** | [**AppServiceDatabaseInput**](AppServiceDatabaseInput.md) |  | [optional] 
**resources** | [**ResourcesInput**](ResourcesInput.md) |  | [optional] 
**scalability** | [**ScalabilityInput**](ScalabilityInput.md) |  | [optional] 

## Example

```python
from wodby.models.new_app_service_input import NewAppServiceInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewAppServiceInput from a JSON string
new_app_service_input_instance = NewAppServiceInput.from_json(json)
# print the JSON string representation of the object
print(NewAppServiceInput.to_json())

# convert the object into a dict
new_app_service_input_dict = new_app_service_input_instance.to_dict()
# create an instance of NewAppServiceInput from a dict
new_app_service_input_from_dict = NewAppServiceInput.from_dict(new_app_service_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


