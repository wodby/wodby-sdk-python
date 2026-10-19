# IntegrationUsagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[IntegrationUsage]**](IntegrationUsage.md) |  | 
**total_count** | **int** |  | 
**next_page** | **int** |  | [optional] 

## Example

```python
from wodby.models.integration_usages_response import IntegrationUsagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationUsagesResponse from a JSON string
integration_usages_response_instance = IntegrationUsagesResponse.from_json(json)
# print the JSON string representation of the object
print(IntegrationUsagesResponse.to_json())

# convert the object into a dict
integration_usages_response_dict = integration_usages_response_instance.to_dict()
# create an instance of IntegrationUsagesResponse from a dict
integration_usages_response_from_dict = IntegrationUsagesResponse.from_dict(integration_usages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


