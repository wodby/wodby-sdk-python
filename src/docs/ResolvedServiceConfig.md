# ResolvedServiceConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | 
**filepath** | **str** |  | 
**manifest_version** | **str** |  | [optional] 
**default_source** | **str** | Whether the default content comes from the service image or its repository. | 
**default_config** | **str** |  | [optional] 
**status** | **str** |  | 
**legacy_fallback** | **bool** |  | 
**image** | **str** |  | [optional] 
**image_digest** | **str** |  | [optional] 
**source_path** | **str** |  | [optional] 
**platform** | **str** |  | 
**error** | **str** |  | [optional] 
**fetched_at** | **datetime** |  | [optional] 

## Example

```python
from wodby.models.resolved_service_config import ResolvedServiceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedServiceConfig from a JSON string
resolved_service_config_instance = ResolvedServiceConfig.from_json(json)
# print the JSON string representation of the object
print(ResolvedServiceConfig.to_json())

# convert the object into a dict
resolved_service_config_dict = resolved_service_config_instance.to_dict()
# create an instance of ResolvedServiceConfig from a dict
resolved_service_config_from_dict = ResolvedServiceConfig.from_dict(resolved_service_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


