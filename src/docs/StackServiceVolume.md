# StackServiceVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**stack_service_id** | **int** |  | 
**name** | **str** |  | 
**size** | **int** |  | 

## Example

```python
from wodby.models.stack_service_volume import StackServiceVolume

# TODO update the JSON string below
json = "{}"
# create an instance of StackServiceVolume from a JSON string
stack_service_volume_instance = StackServiceVolume.from_json(json)
# print the JSON string representation of the object
print(StackServiceVolume.to_json())

# convert the object into a dict
stack_service_volume_dict = stack_service_volume_instance.to_dict()
# create an instance of StackServiceVolume from a dict
stack_service_volume_from_dict = StackServiceVolume.from_dict(stack_service_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


