# IntegrationKind


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**type** | **str** | The integration type in lower case, such as kubernetes, git or registry. | 
**status** | **str** |  | 

## Example

```python
from wodby.models.integration_kind import IntegrationKind

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationKind from a JSON string
integration_kind_instance = IntegrationKind.from_json(json)
# print the JSON string representation of the object
print(IntegrationKind.to_json())

# convert the object into a dict
integration_kind_dict = integration_kind_instance.to_dict()
# create an instance of IntegrationKind from a dict
integration_kind_from_dict = IntegrationKind.from_dict(integration_kind_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


