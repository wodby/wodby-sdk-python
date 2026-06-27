# ConfigOverrideInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 

## Example

```python
from wodby.models.config_override_input import ConfigOverrideInput

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigOverrideInput from a JSON string
config_override_input_instance = ConfigOverrideInput.from_json(json)
# print the JSON string representation of the object
print(ConfigOverrideInput.to_json())

# convert the object into a dict
config_override_input_dict = config_override_input_instance.to_dict()
# create an instance of ConfigOverrideInput from a dict
config_override_input_from_dict = ConfigOverrideInput.from_dict(config_override_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


