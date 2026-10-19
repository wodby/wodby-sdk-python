# AppEnvironmentMigrationComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**app_service_id** | **int** |  | 
**name** | **str** |  | 
**backup_id** | **int** |  | 
**backup_status** | **str** |  | [optional] 
**import_id** | **int** |  | 
**import_status** | **str** |  | [optional] 

## Example

```python
from wodby.models.app_environment_migration_component import AppEnvironmentMigrationComponent

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironmentMigrationComponent from a JSON string
app_environment_migration_component_instance = AppEnvironmentMigrationComponent.from_json(json)
# print the JSON string representation of the object
print(AppEnvironmentMigrationComponent.to_json())

# convert the object into a dict
app_environment_migration_component_dict = app_environment_migration_component_instance.to_dict()
# create an instance of AppEnvironmentMigrationComponent from a dict
app_environment_migration_component_from_dict = AppEnvironmentMigrationComponent.from_dict(app_environment_migration_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


