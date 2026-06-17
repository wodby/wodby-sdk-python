# ResourcesInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workload** | **str** |  | [optional] 
**container** | **str** |  | [optional] 
**request_cpu** | **int** |  | [optional] 
**request_mem** | **int** |  | [optional] 
**limit_cpu** | **int** |  | [optional] 
**limit_mem** | **int** |  | [optional] 

## Example

```python
from wodby.models.resources_input import ResourcesInput

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesInput from a JSON string
resources_input_instance = ResourcesInput.from_json(json)
# print the JSON string representation of the object
print(ResourcesInput.to_json())

# convert the object into a dict
resources_input_dict = resources_input_instance.to_dict()
# create an instance of ResourcesInput from a dict
resources_input_from_dict = ResourcesInput.from_dict(resources_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


