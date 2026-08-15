# IntegrationConfigurationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration** | [**Integration**](Integration.md) |  | 
**task_id** | **int** |  | [optional] 
**warnings** | **List[str]** |  | 

## Example

```python
from wodby.models.integration_configuration_result import IntegrationConfigurationResult

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationConfigurationResult from a JSON string
integration_configuration_result_instance = IntegrationConfigurationResult.from_json(json)
# print the JSON string representation of the object
print(IntegrationConfigurationResult.to_json())

# convert the object into a dict
integration_configuration_result_dict = integration_configuration_result_instance.to_dict()
# create an instance of IntegrationConfigurationResult from a dict
integration_configuration_result_from_dict = IntegrationConfigurationResult.from_dict(integration_configuration_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


