# AppServiceScalability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_cpu** | **int** |  | 
**min_replicas** | **int** |  | 
**max_replicas** | **int** |  | 

## Example

```python
from wodby.models.app_service_scalability import AppServiceScalability

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceScalability from a JSON string
app_service_scalability_instance = AppServiceScalability.from_json(json)
# print the JSON string representation of the object
print(AppServiceScalability.to_json())

# convert the object into a dict
app_service_scalability_dict = app_service_scalability_instance.to_dict()
# create an instance of AppServiceScalability from a dict
app_service_scalability_from_dict = AppServiceScalability.from_dict(app_service_scalability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


