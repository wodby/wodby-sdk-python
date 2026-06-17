# ScalabilityInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_cpu** | **int** |  | 
**min_replicas** | **int** |  | 
**max_replicas** | **int** |  | 

## Example

```python
from wodby.models.scalability_input import ScalabilityInput

# TODO update the JSON string below
json = "{}"
# create an instance of ScalabilityInput from a JSON string
scalability_input_instance = ScalabilityInput.from_json(json)
# print the JSON string representation of the object
print(ScalabilityInput.to_json())

# convert the object into a dict
scalability_input_dict = scalability_input_instance.to_dict()
# create an instance of ScalabilityInput from a dict
scalability_input_from_dict = ScalabilityInput.from_dict(scalability_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


