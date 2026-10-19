# AppEnvironmentMigrationOperationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**task_id** | **int** | Task that runs the requested step. | [optional] 
**migration** | [**AppEnvironmentMigration**](AppEnvironmentMigration.md) |  | 

## Example

```python
from wodby.models.app_environment_migration_operation_result import AppEnvironmentMigrationOperationResult

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironmentMigrationOperationResult from a JSON string
app_environment_migration_operation_result_instance = AppEnvironmentMigrationOperationResult.from_json(json)
# print the JSON string representation of the object
print(AppEnvironmentMigrationOperationResult.to_json())

# convert the object into a dict
app_environment_migration_operation_result_dict = app_environment_migration_operation_result_instance.to_dict()
# create an instance of AppEnvironmentMigrationOperationResult from a dict
app_environment_migration_operation_result_from_dict = AppEnvironmentMigrationOperationResult.from_dict(app_environment_migration_operation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


