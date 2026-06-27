# UpdateStackServiceTokenInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**secret** | **bool** |  | 
**regex** | **str** |  | [optional] 

## Example

```python
from wodby.models.update_stack_service_token_input import UpdateStackServiceTokenInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStackServiceTokenInput from a JSON string
update_stack_service_token_input_instance = UpdateStackServiceTokenInput.from_json(json)
# print the JSON string representation of the object
print(UpdateStackServiceTokenInput.to_json())

# convert the object into a dict
update_stack_service_token_input_dict = update_stack_service_token_input_instance.to_dict()
# create an instance of UpdateStackServiceTokenInput from a dict
update_stack_service_token_input_from_dict = UpdateStackServiceTokenInput.from_dict(update_stack_service_token_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


