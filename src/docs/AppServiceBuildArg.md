# AppServiceBuildArg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 
**secret** | **bool** |  | 

## Example

```python
from wodby.models.app_service_build_arg import AppServiceBuildArg

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceBuildArg from a JSON string
app_service_build_arg_instance = AppServiceBuildArg.from_json(json)
# print the JSON string representation of the object
print(AppServiceBuildArg.to_json())

# convert the object into a dict
app_service_build_arg_dict = app_service_build_arg_instance.to_dict()
# create an instance of AppServiceBuildArg from a dict
app_service_build_arg_from_dict = AppServiceBuildArg.from_dict(app_service_build_arg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


