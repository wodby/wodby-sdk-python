# StackServiceConfigInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **str** |  | 

## Example

```python
from wodby.models.stack_service_config_input import StackServiceConfigInput

# TODO update the JSON string below
json = "{}"
# create an instance of StackServiceConfigInput from a JSON string
stack_service_config_input_instance = StackServiceConfigInput.from_json(json)
# print the JSON string representation of the object
print(StackServiceConfigInput.to_json())

# convert the object into a dict
stack_service_config_input_dict = stack_service_config_input_instance.to_dict()
# create an instance of StackServiceConfigInput from a dict
stack_service_config_input_from_dict = StackServiceConfigInput.from_dict(stack_service_config_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


