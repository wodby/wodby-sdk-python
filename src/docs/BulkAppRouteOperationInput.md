# BulkAppRouteOperationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_environment_id** | **int** |  | 
**route_ids** | **List[int]** | Routes of the app environment to change. | 
**operation** | **str** |  | 

## Example

```python
from wodby.models.bulk_app_route_operation_input import BulkAppRouteOperationInput

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAppRouteOperationInput from a JSON string
bulk_app_route_operation_input_instance = BulkAppRouteOperationInput.from_json(json)
# print the JSON string representation of the object
print(BulkAppRouteOperationInput.to_json())

# convert the object into a dict
bulk_app_route_operation_input_dict = bulk_app_route_operation_input_instance.to_dict()
# create an instance of BulkAppRouteOperationInput from a dict
bulk_app_route_operation_input_from_dict = BulkAppRouteOperationInput.from_dict(bulk_app_route_operation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


