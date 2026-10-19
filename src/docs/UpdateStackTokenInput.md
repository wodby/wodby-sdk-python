# UpdateStackTokenInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**secret** | **bool** |  | 
**regex** | **str** |  | [optional] 

## Example

```python
from wodby.models.update_stack_token_input import UpdateStackTokenInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStackTokenInput from a JSON string
update_stack_token_input_instance = UpdateStackTokenInput.from_json(json)
# print the JSON string representation of the object
print(UpdateStackTokenInput.to_json())

# convert the object into a dict
update_stack_token_input_dict = update_stack_token_input_instance.to_dict()
# create an instance of UpdateStackTokenInput from a dict
update_stack_token_input_from_dict = UpdateStackTokenInput.from_dict(update_stack_token_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


