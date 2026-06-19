# AppBuildConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registry_host** | **str** |  | 
**registry_repository** | **str** |  | 
**services** | [**List[AppServiceBuildConfig]**](AppServiceBuildConfig.md) |  | 

## Example

```python
from wodby.models.app_build_config import AppBuildConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppBuildConfig from a JSON string
app_build_config_instance = AppBuildConfig.from_json(json)
# print the JSON string representation of the object
print(AppBuildConfig.to_json())

# convert the object into a dict
app_build_config_dict = app_build_config_instance.to_dict()
# create an instance of AppBuildConfig from a dict
app_build_config_from_dict = AppBuildConfig.from_dict(app_build_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


