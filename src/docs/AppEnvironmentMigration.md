# AppEnvironmentMigration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**app_environment_id** | **int** |  | 
**source_cluster_id** | **int** |  | 
**target_cluster_id** | **int** |  | 
**task_id** | **int** | Task that runs the migration. | 
**deployment_id** | **int** | Deployment that brings the environment up on the target cluster. | [optional] 
**status** | **str** |  | 
**phase** | **str** |  | 
**components** | [**List[AppEnvironmentMigrationComponent]**](AppEnvironmentMigrationComponent.md) | Services whose data the migration copies with a backup on the source and an import on the target. | 
**failure_message** | **str** |  | 
**retain_until** | **datetime** | When the retained source is removed automatically. | [optional] 
**cutover_at** | **datetime** |  | [optional] 
**ended_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.app_environment_migration import AppEnvironmentMigration

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironmentMigration from a JSON string
app_environment_migration_instance = AppEnvironmentMigration.from_json(json)
# print the JSON string representation of the object
print(AppEnvironmentMigration.to_json())

# convert the object into a dict
app_environment_migration_dict = app_environment_migration_instance.to_dict()
# create an instance of AppEnvironmentMigration from a dict
app_environment_migration_from_dict = AppEnvironmentMigration.from_dict(app_environment_migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


