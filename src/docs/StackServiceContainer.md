# StackServiceContainer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**stack_service_id** | **int** |  | 
**workload** | **str** |  | 
**name** | **str** |  | 
**request_cpu** | **int** |  | [optional] 
**request_mem** | **int** |  | [optional] 
**limit_cpu** | **int** |  | [optional] 
**limit_mem** | **int** |  | [optional] 

## Example

```python
from wodby.models.stack_service_container import StackServiceContainer

# TODO update the JSON string below
json = "{}"
# create an instance of StackServiceContainer from a JSON string
stack_service_container_instance = StackServiceContainer.from_json(json)
# print the JSON string representation of the object
print(StackServiceContainer.to_json())

# convert the object into a dict
stack_service_container_dict = stack_service_container_instance.to_dict()
# create an instance of StackServiceContainer from a dict
stack_service_container_from_dict = StackServiceContainer.from_dict(stack_service_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


