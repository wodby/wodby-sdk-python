# AppServiceCapacityPreflightRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_usage** | **int** | Number of enabled app services the operation would add. | 

## Example

```python
from wodby.models.app_service_capacity_preflight_request import AppServiceCapacityPreflightRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceCapacityPreflightRequest from a JSON string
app_service_capacity_preflight_request_instance = AppServiceCapacityPreflightRequest.from_json(json)
# print the JSON string representation of the object
print(AppServiceCapacityPreflightRequest.to_json())

# convert the object into a dict
app_service_capacity_preflight_request_dict = app_service_capacity_preflight_request_instance.to_dict()
# create an instance of AppServiceCapacityPreflightRequest from a dict
app_service_capacity_preflight_request_from_dict = AppServiceCapacityPreflightRequest.from_dict(app_service_capacity_preflight_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


