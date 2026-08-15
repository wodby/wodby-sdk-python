# ResolveIntegrationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration** | [**Integration**](Integration.md) |  | 
**created** | **bool** |  | 

## Example

```python
from wodby.models.resolve_integration_result import ResolveIntegrationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ResolveIntegrationResult from a JSON string
resolve_integration_result_instance = ResolveIntegrationResult.from_json(json)
# print the JSON string representation of the object
print(ResolveIntegrationResult.to_json())

# convert the object into a dict
resolve_integration_result_dict = resolve_integration_result_instance.to_dict()
# create an instance of ResolveIntegrationResult from a dict
resolve_integration_result_from_dict = ResolveIntegrationResult.from_dict(resolve_integration_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


