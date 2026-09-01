# AppServiceInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replicas** | **int** |  | [optional] 
**scalability** | [**AppServiceScalabilityUpdateInput**](AppServiceScalabilityUpdateInput.md) |  | [optional] 
**version** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**main** | **bool** |  | [optional] 
**build_source** | [**BuildSourceInput**](BuildSourceInput.md) |  | [optional] 
**deployment** | [**ServiceDeploymentConfigurationInput**](ServiceDeploymentConfigurationInput.md) |  | [optional] 

## Example

```python
from wodby.models.app_service_input import AppServiceInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceInput from a JSON string
app_service_input_instance = AppServiceInput.from_json(json)
# print the JSON string representation of the object
print(AppServiceInput.to_json())

# convert the object into a dict
app_service_input_dict = app_service_input_instance.to_dict()
# create an instance of AppServiceInput from a dict
app_service_input_from_dict = AppServiceInput.from_dict(app_service_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


