# AppServiceIntegrationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**integration_ids** | **List[int]** |  | 

## Example

```python
from wodby.models.app_service_integration_input import AppServiceIntegrationInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceIntegrationInput from a JSON string
app_service_integration_input_instance = AppServiceIntegrationInput.from_json(json)
# print the JSON string representation of the object
print(AppServiceIntegrationInput.to_json())

# convert the object into a dict
app_service_integration_input_dict = app_service_integration_input_instance.to_dict()
# create an instance of AppServiceIntegrationInput from a dict
app_service_integration_input_from_dict = AppServiceIntegrationInput.from_dict(app_service_integration_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


