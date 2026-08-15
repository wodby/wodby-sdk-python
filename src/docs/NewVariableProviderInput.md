# NewVariableProviderInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** | Optional for API-key requests; defaults to the API key&#39;s organization. | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | 
**title** | **str** |  | 
**fields** | [**List[NewVariableProviderFieldInput]**](NewVariableProviderFieldInput.md) |  | 

## Example

```python
from wodby.models.new_variable_provider_input import NewVariableProviderInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewVariableProviderInput from a JSON string
new_variable_provider_input_instance = NewVariableProviderInput.from_json(json)
# print the JSON string representation of the object
print(NewVariableProviderInput.to_json())

# convert the object into a dict
new_variable_provider_input_dict = new_variable_provider_input_instance.to_dict()
# create an instance of NewVariableProviderInput from a dict
new_variable_provider_input_from_dict = NewVariableProviderInput.from_dict(new_variable_provider_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


