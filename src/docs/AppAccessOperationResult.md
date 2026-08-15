# AppAccessOperationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**AppAccess**](AppAccess.md) |  | 
**task_id** | **int** |  | [optional] 

## Example

```python
from wodby.models.app_access_operation_result import AppAccessOperationResult

# TODO update the JSON string below
json = "{}"
# create an instance of AppAccessOperationResult from a JSON string
app_access_operation_result_instance = AppAccessOperationResult.from_json(json)
# print the JSON string representation of the object
print(AppAccessOperationResult.to_json())

# convert the object into a dict
app_access_operation_result_dict = app_access_operation_result_instance.to_dict()
# create an instance of AppAccessOperationResult from a dict
app_access_operation_result_from_dict = AppAccessOperationResult.from_dict(app_access_operation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


