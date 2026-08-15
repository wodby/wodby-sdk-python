# NewAppInstanceAccessInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **int** |  | 
**mode** | **str** |  | 
**scope** | **str** |  | 
**settings** | [**List[AppAccessSettingInput]**](AppAccessSettingInput.md) |  | [optional] 
**host** | **str** | Required only when the selected provider uses a customer-assigned hostname. | [optional] 
**endpoints** | [**List[NewAppInstanceAccessEndpointInput]**](NewAppInstanceAccessEndpointInput.md) | HTTP endpoints selected during creation. Used only with SELECTED_ENDPOINTS scope; older clients may omit it to select the main endpoint. | [optional] 

## Example

```python
from wodby.models.new_app_instance_access_input import NewAppInstanceAccessInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewAppInstanceAccessInput from a JSON string
new_app_instance_access_input_instance = NewAppInstanceAccessInput.from_json(json)
# print the JSON string representation of the object
print(NewAppInstanceAccessInput.to_json())

# convert the object into a dict
new_app_instance_access_input_dict = new_app_instance_access_input_instance.to_dict()
# create an instance of NewAppInstanceAccessInput from a dict
new_app_instance_access_input_from_dict = NewAppInstanceAccessInput.from_dict(new_app_instance_access_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


