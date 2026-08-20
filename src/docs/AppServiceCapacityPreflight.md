# AppServiceCapacityPreflight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | **bool** | Whether the proposed usage increase is permitted by the effective backend policy. | 
**enforced** | **bool** | Whether subscription capacity limits apply to this organization. | 
**usage** | **float** |  | 
**usage_included** | **float** |  | 
**projected_usage** | **float** |  | 

## Example

```python
from wodby.models.app_service_capacity_preflight import AppServiceCapacityPreflight

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceCapacityPreflight from a JSON string
app_service_capacity_preflight_instance = AppServiceCapacityPreflight.from_json(json)
# print the JSON string representation of the object
print(AppServiceCapacityPreflight.to_json())

# convert the object into a dict
app_service_capacity_preflight_dict = app_service_capacity_preflight_instance.to_dict()
# create an instance of AppServiceCapacityPreflight from a dict
app_service_capacity_preflight_from_dict = AppServiceCapacityPreflight.from_dict(app_service_capacity_preflight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


