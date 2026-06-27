# StackServiceIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**stack_service_id** | **int** |  | 
**name** | **str** |  | 
**integration_id** | **int** |  | 

## Example

```python
from wodby.models.stack_service_integration import StackServiceIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of StackServiceIntegration from a JSON string
stack_service_integration_instance = StackServiceIntegration.from_json(json)
# print the JSON string representation of the object
print(StackServiceIntegration.to_json())

# convert the object into a dict
stack_service_integration_dict = stack_service_integration_instance.to_dict()
# create an instance of StackServiceIntegration from a dict
stack_service_integration_from_dict = StackServiceIntegration.from_dict(stack_service_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


