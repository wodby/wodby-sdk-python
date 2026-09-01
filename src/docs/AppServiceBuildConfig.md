# AppServiceBuildConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | 
**managed** | **bool** |  | 
**main** | **bool** |  | 
**image** | **str** |  | 
**dockerfile** | **str** |  | [optional] 
**dockerignore** | **str** |  | [optional] 
**copy_subdir** | **str** | Resolved subdirectory this build copies, applied under both the CI --from and --to paths. Empty means the whole context. | 
**args** | [**List[AppServiceBuildArg]**](AppServiceBuildArg.md) |  | [optional] 

## Example

```python
from wodby.models.app_service_build_config import AppServiceBuildConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceBuildConfig from a JSON string
app_service_build_config_instance = AppServiceBuildConfig.from_json(json)
# print the JSON string representation of the object
print(AppServiceBuildConfig.to_json())

# convert the object into a dict
app_service_build_config_dict = app_service_build_config_instance.to_dict()
# create an instance of AppServiceBuildConfig from a dict
app_service_build_config_from_dict = AppServiceBuildConfig.from_dict(app_service_build_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


