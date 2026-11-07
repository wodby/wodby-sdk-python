# ResourcePreset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Set only for an organization&#39;s custom presets. | [optional] 
**name** | **str** |  | 
**title** | **str** |  | 
**request_cpu** | **int** | Requested CPU in millicores. | [optional] 
**request_mem** | **int** | Requested memory in MiB. | [optional] 
**limit_cpu** | **int** | CPU limit in millicores. | [optional] 
**limit_mem** | **int** | Memory limit in MiB. | [optional] 
**system** | **bool** | Wodby&#39;s own presets, whose values never change. | 

## Example

```python
from wodby.models.resource_preset import ResourcePreset

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePreset from a JSON string
resource_preset_instance = ResourcePreset.from_json(json)
# print the JSON string representation of the object
print(ResourcePreset.to_json())

# convert the object into a dict
resource_preset_dict = resource_preset_instance.to_dict()
# create an instance of ResourcePreset from a dict
resource_preset_from_dict = ResourcePreset.from_dict(resource_preset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


