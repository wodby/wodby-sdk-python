# NewStackServiceTokenInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | [optional] 
**secret** | **bool** |  | 
**regex** | **str** |  | [optional] 
**env_type** | **str** |  | [optional] 

## Example

```python
from wodby.models.new_stack_service_token_input import NewStackServiceTokenInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewStackServiceTokenInput from a JSON string
new_stack_service_token_input_instance = NewStackServiceTokenInput.from_json(json)
# print the JSON string representation of the object
print(NewStackServiceTokenInput.to_json())

# convert the object into a dict
new_stack_service_token_input_dict = new_stack_service_token_input_instance.to_dict()
# create an instance of NewStackServiceTokenInput from a dict
new_stack_service_token_input_from_dict = NewStackServiceTokenInput.from_dict(new_stack_service_token_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


