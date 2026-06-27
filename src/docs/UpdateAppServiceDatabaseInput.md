# UpdateAppServiceDatabaseInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_db_id** | **int** |  | [optional] 
**database_user_id** | **int** |  | [optional] 

## Example

```python
from wodby.models.update_app_service_database_input import UpdateAppServiceDatabaseInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAppServiceDatabaseInput from a JSON string
update_app_service_database_input_instance = UpdateAppServiceDatabaseInput.from_json(json)
# print the JSON string representation of the object
print(UpdateAppServiceDatabaseInput.to_json())

# convert the object into a dict
update_app_service_database_input_dict = update_app_service_database_input_instance.to_dict()
# create an instance of UpdateAppServiceDatabaseInput from a dict
update_app_service_database_input_from_dict = UpdateAppServiceDatabaseInput.from_dict(update_app_service_database_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


