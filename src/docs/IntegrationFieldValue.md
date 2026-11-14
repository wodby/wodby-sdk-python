# IntegrationFieldValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**var_field** | **str** |  | 
**value** | **str** | The field&#39;s value. Null for a secret field. | [optional] 

## Example

```python
from wodby.models.integration_field_value import IntegrationFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationFieldValue from a JSON string
integration_field_value_instance = IntegrationFieldValue.from_json(json)
# print the JSON string representation of the object
print(IntegrationFieldValue.to_json())

# convert the object into a dict
integration_field_value_dict = integration_field_value_instance.to_dict()
# create an instance of IntegrationFieldValue from a dict
integration_field_value_from_dict = IntegrationFieldValue.from_dict(integration_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


