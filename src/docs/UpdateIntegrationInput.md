# UpdateIntegrationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**name** | **str** |  | 
**kinds** | **List[str]** |  | 
**scope** | **str** |  | [optional] 
**fields_input** | [**List[FieldInput]**](FieldInput.md) |  | [optional] 

## Example

```python
from wodby.models.update_integration_input import UpdateIntegrationInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIntegrationInput from a JSON string
update_integration_input_instance = UpdateIntegrationInput.from_json(json)
# print the JSON string representation of the object
print(UpdateIntegrationInput.to_json())

# convert the object into a dict
update_integration_input_dict = update_integration_input_instance.to_dict()
# create an instance of UpdateIntegrationInput from a dict
update_integration_input_from_dict = UpdateIntegrationInput.from_dict(update_integration_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


