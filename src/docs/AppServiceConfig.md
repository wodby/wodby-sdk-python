# AppServiceConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**app_service_id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**config** | **str** |  | [optional] 
**disabled** | **bool** |  | 

## Example

```python
from wodby.models.app_service_config import AppServiceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceConfig from a JSON string
app_service_config_instance = AppServiceConfig.from_json(json)
# print the JSON string representation of the object
print(AppServiceConfig.to_json())

# convert the object into a dict
app_service_config_dict = app_service_config_instance.to_dict()
# create an instance of AppServiceConfig from a dict
app_service_config_from_dict = AppServiceConfig.from_dict(app_service_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


