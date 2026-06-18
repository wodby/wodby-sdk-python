# AppServiceDatabaseInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_id** | **int** |  | 
**database_db_id** | **int** |  | [optional] 

## Example

```python
from wodby.models.app_service_database_input import AppServiceDatabaseInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceDatabaseInput from a JSON string
app_service_database_input_instance = AppServiceDatabaseInput.from_json(json)
# print the JSON string representation of the object
print(AppServiceDatabaseInput.to_json())

# convert the object into a dict
app_service_database_input_dict = app_service_database_input_instance.to_dict()
# create an instance of AppServiceDatabaseInput from a dict
app_service_database_input_from_dict = AppServiceDatabaseInput.from_dict(app_service_database_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


