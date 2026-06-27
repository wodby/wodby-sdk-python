# StackServiceConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**stack_service_id** | **int** |  | 
**name** | **str** |  | 
**config** | **str** |  | 
**disabled** | **bool** |  | 

## Example

```python
from wodby.models.stack_service_config import StackServiceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of StackServiceConfig from a JSON string
stack_service_config_instance = StackServiceConfig.from_json(json)
# print the JSON string representation of the object
print(StackServiceConfig.to_json())

# convert the object into a dict
stack_service_config_dict = stack_service_config_instance.to_dict()
# create an instance of StackServiceConfig from a dict
stack_service_config_from_dict = StackServiceConfig.from_dict(stack_service_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


