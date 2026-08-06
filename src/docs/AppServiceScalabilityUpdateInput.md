# AppServiceScalabilityUpdateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**average_cpu** | **int** |  | [optional] 
**min_replicas** | **int** |  | [optional] 
**max_replicas** | **int** |  | [optional] 

## Example

```python
from wodby.models.app_service_scalability_update_input import AppServiceScalabilityUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceScalabilityUpdateInput from a JSON string
app_service_scalability_update_input_instance = AppServiceScalabilityUpdateInput.from_json(json)
# print the JSON string representation of the object
print(AppServiceScalabilityUpdateInput.to_json())

# convert the object into a dict
app_service_scalability_update_input_dict = app_service_scalability_update_input_instance.to_dict()
# create an instance of AppServiceScalabilityUpdateInput from a dict
app_service_scalability_update_input_from_dict = AppServiceScalabilityUpdateInput.from_dict(app_service_scalability_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


