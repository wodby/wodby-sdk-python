# AppEnvironmentMigrationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_cluster_id** | **int** | Cluster of the same organization that the environment moves to. | 
**volumes** | [**List[AppEnvironmentMigrationVolumeInput]**](AppEnvironmentMigrationVolumeInput.md) | Target cluster storage classes for the environment&#39;s volumes. A volume left out uses its current storage class, which must exist on the target cluster. | [optional] 
**existing_backup_ids** | **List[int]** | Completed backups of this environment to restore instead of creating final backups. Data written after a backup was taken does not reach the target. Components without a backup listed here get a final backup. | [optional] 

## Example

```python
from wodby.models.app_environment_migration_input import AppEnvironmentMigrationInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironmentMigrationInput from a JSON string
app_environment_migration_input_instance = AppEnvironmentMigrationInput.from_json(json)
# print the JSON string representation of the object
print(AppEnvironmentMigrationInput.to_json())

# convert the object into a dict
app_environment_migration_input_dict = app_environment_migration_input_instance.to_dict()
# create an instance of AppEnvironmentMigrationInput from a dict
app_environment_migration_input_from_dict = AppEnvironmentMigrationInput.from_dict(app_environment_migration_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


