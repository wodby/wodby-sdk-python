# NewAppServiceOverrideInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Stack service ID in the selected stack revision. | 
**disabled** | **bool** |  | [optional] 
**version** | **str** |  | [optional] 
**build_source** | [**BuildSourceInput**](BuildSourceInput.md) |  | [optional] 
**settings** | [**List[AppServiceSettingInput]**](AppServiceSettingInput.md) | Service settings to set. A setting that is not named keeps its default. Use it to supply a required setting that has no default. | [optional] 
**database** | [**AppServiceDatabaseInput**](AppServiceDatabaseInput.md) | The database server, and optionally the database, of a database service. Required to enable an external database service, such as a managed PostgreSQL server. | [optional] 

## Example

```python
from wodby.models.new_app_service_override_input import NewAppServiceOverrideInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewAppServiceOverrideInput from a JSON string
new_app_service_override_input_instance = NewAppServiceOverrideInput.from_json(json)
# print the JSON string representation of the object
print(NewAppServiceOverrideInput.to_json())

# convert the object into a dict
new_app_service_override_input_dict = new_app_service_override_input_instance.to_dict()
# create an instance of NewAppServiceOverrideInput from a dict
new_app_service_override_input_from_dict = NewAppServiceOverrideInput.from_dict(new_app_service_override_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


