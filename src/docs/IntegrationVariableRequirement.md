# IntegrationVariableRequirement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**secret** | **bool** |  | 
**optional** | **bool** |  | 

## Example

```python
from wodby.models.integration_variable_requirement import IntegrationVariableRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationVariableRequirement from a JSON string
integration_variable_requirement_instance = IntegrationVariableRequirement.from_json(json)
# print the JSON string representation of the object
print(IntegrationVariableRequirement.to_json())

# convert the object into a dict
integration_variable_requirement_dict = integration_variable_requirement_instance.to_dict()
# create an instance of IntegrationVariableRequirement from a dict
integration_variable_requirement_from_dict = IntegrationVariableRequirement.from_dict(integration_variable_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


