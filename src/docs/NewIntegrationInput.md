# NewIntegrationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** |  | 
**provider_id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**kinds** | **List[str]** |  | 
**auth** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**fields_input** | [**List[FieldInput]**](FieldInput.md) |  | [optional] 
**scope** | **str** |  | [optional] 

## Example

```python
from wodby.models.new_integration_input import NewIntegrationInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewIntegrationInput from a JSON string
new_integration_input_instance = NewIntegrationInput.from_json(json)
# print the JSON string representation of the object
print(NewIntegrationInput.to_json())

# convert the object into a dict
new_integration_input_dict = new_integration_input_instance.to_dict()
# create an instance of NewIntegrationInput from a dict
new_integration_input_from_dict = NewIntegrationInput.from_dict(new_integration_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


