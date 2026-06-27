# AppServiceHelmValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**app_service_id** | **int** |  | 
**name** | **str** |  | 
**value** | **str** |  | 
**value_secret_id** | **int** |  | [optional] 
**source** | [**AppServiceHelmValueSource**](AppServiceHelmValueSource.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from wodby.models.app_service_helm_value import AppServiceHelmValue

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceHelmValue from a JSON string
app_service_helm_value_instance = AppServiceHelmValue.from_json(json)
# print the JSON string representation of the object
print(AppServiceHelmValue.to_json())

# convert the object into a dict
app_service_helm_value_dict = app_service_helm_value_instance.to_dict()
# create an instance of AppServiceHelmValue from a dict
app_service_helm_value_from_dict = AppServiceHelmValue.from_dict(app_service_helm_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


