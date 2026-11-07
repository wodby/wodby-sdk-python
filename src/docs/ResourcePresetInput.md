# ResourcePresetInput

Set at least one value. CPU is in millicores (multiples of 10), memory in MiB (multiples of 16).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** | Used when creating a preset. Optional for API-key requests; defaults to the API key&#39;s organization. | [optional] 
**name** | **str** | Lowercase letters, digits and dashes; unique in the organization and not the name of a Wodby preset. | 
**title** | **str** |  | 
**request_cpu** | **int** |  | [optional] 
**request_mem** | **int** |  | [optional] 
**limit_cpu** | **int** |  | [optional] 
**limit_mem** | **int** |  | [optional] 

## Example

```python
from wodby.models.resource_preset_input import ResourcePresetInput

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePresetInput from a JSON string
resource_preset_input_instance = ResourcePresetInput.from_json(json)
# print the JSON string representation of the object
print(ResourcePresetInput.to_json())

# convert the object into a dict
resource_preset_input_dict = resource_preset_input_instance.to_dict()
# create an instance of ResourcePresetInput from a dict
resource_preset_input_from_dict = ResourcePresetInput.from_dict(resource_preset_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


