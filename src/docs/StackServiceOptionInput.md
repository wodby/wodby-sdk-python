# StackServiceOptionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**default** | **bool** |  | 
**disabled** | **bool** |  | 

## Example

```python
from wodby.models.stack_service_option_input import StackServiceOptionInput

# TODO update the JSON string below
json = "{}"
# create an instance of StackServiceOptionInput from a JSON string
stack_service_option_input_instance = StackServiceOptionInput.from_json(json)
# print the JSON string representation of the object
print(StackServiceOptionInput.to_json())

# convert the object into a dict
stack_service_option_input_dict = stack_service_option_input_instance.to_dict()
# create an instance of StackServiceOptionInput from a dict
stack_service_option_input_from_dict = StackServiceOptionInput.from_dict(stack_service_option_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


