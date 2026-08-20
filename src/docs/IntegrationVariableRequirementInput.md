# IntegrationVariableRequirementInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**secret** | **bool** |  | [optional] [default to False]
**optional** | **bool** |  | [optional] [default to False]

## Example

```python
from wodby.models.integration_variable_requirement_input import IntegrationVariableRequirementInput

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationVariableRequirementInput from a JSON string
integration_variable_requirement_input_instance = IntegrationVariableRequirementInput.from_json(json)
# print the JSON string representation of the object
print(IntegrationVariableRequirementInput.to_json())

# convert the object into a dict
integration_variable_requirement_input_dict = integration_variable_requirement_input_instance.to_dict()
# create an instance of IntegrationVariableRequirementInput from a dict
integration_variable_requirement_input_from_dict = IntegrationVariableRequirementInput.from_dict(integration_variable_requirement_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


