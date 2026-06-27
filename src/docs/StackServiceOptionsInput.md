# StackServiceOptionsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**List[StackServiceOptionInput]**](StackServiceOptionInput.md) |  | 

## Example

```python
from wodby.models.stack_service_options_input import StackServiceOptionsInput

# TODO update the JSON string below
json = "{}"
# create an instance of StackServiceOptionsInput from a JSON string
stack_service_options_input_instance = StackServiceOptionsInput.from_json(json)
# print the JSON string representation of the object
print(StackServiceOptionsInput.to_json())

# convert the object into a dict
stack_service_options_input_dict = stack_service_options_input_instance.to_dict()
# create an instance of StackServiceOptionsInput from a dict
stack_service_options_input_from_dict = StackServiceOptionsInput.from_dict(stack_service_options_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


