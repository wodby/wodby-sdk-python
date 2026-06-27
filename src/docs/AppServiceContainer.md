# AppServiceContainer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**app_service_id** | **int** |  | 
**workload** | **str** |  | 
**name** | **str** |  | 
**request_cpu** | **int** |  | [optional] 
**request_mem** | **int** |  | [optional] 
**limit_cpu** | **int** |  | [optional] 
**limit_mem** | **int** |  | [optional] 

## Example

```python
from wodby.models.app_service_container import AppServiceContainer

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceContainer from a JSON string
app_service_container_instance = AppServiceContainer.from_json(json)
# print the JSON string representation of the object
print(AppServiceContainer.to_json())

# convert the object into a dict
app_service_container_dict = app_service_container_instance.to_dict()
# create an instance of AppServiceContainer from a dict
app_service_container_from_dict = AppServiceContainer.from_dict(app_service_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


