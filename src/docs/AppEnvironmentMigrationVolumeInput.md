# AppEnvironmentMigrationVolumeInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_service_volume_id** | **int** |  | 
**storage_class_name** | **str** | Target cluster storage class for the volume. | [optional] 

## Example

```python
from wodby.models.app_environment_migration_volume_input import AppEnvironmentMigrationVolumeInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironmentMigrationVolumeInput from a JSON string
app_environment_migration_volume_input_instance = AppEnvironmentMigrationVolumeInput.from_json(json)
# print the JSON string representation of the object
print(AppEnvironmentMigrationVolumeInput.to_json())

# convert the object into a dict
app_environment_migration_volume_input_dict = app_environment_migration_volume_input_instance.to_dict()
# create an instance of AppEnvironmentMigrationVolumeInput from a dict
app_environment_migration_volume_input_from_dict = AppEnvironmentMigrationVolumeInput.from_dict(app_environment_migration_volume_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


