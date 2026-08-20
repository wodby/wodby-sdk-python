# ServiceIntegrationRequirement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | 
**type** | **str** |  | 
**labels** | **List[str]** |  | [optional] 
**variables** | [**List[IntegrationVariableRequirement]**](IntegrationVariableRequirement.md) |  | 
**required** | **bool** |  | 
**multiple** | **bool** |  | 

## Example

```python
from wodby.models.service_integration_requirement import ServiceIntegrationRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceIntegrationRequirement from a JSON string
service_integration_requirement_instance = ServiceIntegrationRequirement.from_json(json)
# print the JSON string representation of the object
print(ServiceIntegrationRequirement.to_json())

# convert the object into a dict
service_integration_requirement_dict = service_integration_requirement_instance.to_dict()
# create an instance of ServiceIntegrationRequirement from a dict
service_integration_requirement_from_dict = ServiceIntegrationRequirement.from_dict(service_integration_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


