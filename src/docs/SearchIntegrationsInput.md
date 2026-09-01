# SearchIntegrationsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** | Optional for API-key requests; defaults to the API key&#39;s organization. | [optional] 
**project_ids** | **List[int]** |  | [optional] 
**types** | **List[str]** |  | [optional] 
**statuses** | **List[str]** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**variables** | [**List[IntegrationVariableRequirementInput]**](IntegrationVariableRequirementInput.md) |  | [optional] 
**env_id** | **int** |  | [optional] 
**env_type** | **str** |  | [optional] 

## Example

```python
from wodby.models.search_integrations_input import SearchIntegrationsInput

# TODO update the JSON string below
json = "{}"
# create an instance of SearchIntegrationsInput from a JSON string
search_integrations_input_instance = SearchIntegrationsInput.from_json(json)
# print the JSON string representation of the object
print(SearchIntegrationsInput.to_json())

# convert the object into a dict
search_integrations_input_dict = search_integrations_input_instance.to_dict()
# create an instance of SearchIntegrationsInput from a dict
search_integrations_input_from_dict = SearchIntegrationsInput.from_dict(search_integrations_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


