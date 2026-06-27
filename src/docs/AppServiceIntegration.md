# AppServiceIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**app_service_id** | **int** |  | 
**name** | **str** |  | 
**integration_id** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.app_service_integration import AppServiceIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceIntegration from a JSON string
app_service_integration_instance = AppServiceIntegration.from_json(json)
# print the JSON string representation of the object
print(AppServiceIntegration.to_json())

# convert the object into a dict
app_service_integration_dict = app_service_integration_instance.to_dict()
# create an instance of AppServiceIntegration from a dict
app_service_integration_from_dict = AppServiceIntegration.from_dict(app_service_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


