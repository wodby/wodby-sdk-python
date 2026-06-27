# IntegrationLinkInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**integration_id** | **int** |  | 

## Example

```python
from wodby.models.integration_link_input import IntegrationLinkInput

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationLinkInput from a JSON string
integration_link_input_instance = IntegrationLinkInput.from_json(json)
# print the JSON string representation of the object
print(IntegrationLinkInput.to_json())

# convert the object into a dict
integration_link_input_dict = integration_link_input_instance.to_dict()
# create an instance of IntegrationLinkInput from a dict
integration_link_input_from_dict = IntegrationLinkInput.from_dict(integration_link_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


