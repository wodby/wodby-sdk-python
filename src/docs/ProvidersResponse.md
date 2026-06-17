# ProvidersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Provider]**](Provider.md) |  | 
**total_count** | **int** |  | 
**next_page** | **int** |  | [optional] 

## Example

```python
from wodby.models.providers_response import ProvidersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProvidersResponse from a JSON string
providers_response_instance = ProvidersResponse.from_json(json)
# print the JSON string representation of the object
print(ProvidersResponse.to_json())

# convert the object into a dict
providers_response_dict = providers_response_instance.to_dict()
# create an instance of ProvidersResponse from a dict
providers_response_from_dict = ProvidersResponse.from_dict(providers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


