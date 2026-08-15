# NewAppAccessInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **int** |  | 
**mode** | **str** |  | 
**scope** | **str** |  | 
**settings** | [**List[AppAccessSettingInput]**](AppAccessSettingInput.md) |  | [optional] 
**endpoints** | [**List[AppAccessEndpointInput]**](AppAccessEndpointInput.md) |  | 

## Example

```python
from wodby.models.new_app_access_input import NewAppAccessInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewAppAccessInput from a JSON string
new_app_access_input_instance = NewAppAccessInput.from_json(json)
# print the JSON string representation of the object
print(NewAppAccessInput.to_json())

# convert the object into a dict
new_app_access_input_dict = new_app_access_input_instance.to_dict()
# create an instance of NewAppAccessInput from a dict
new_app_access_input_from_dict = NewAppAccessInput.from_dict(new_app_access_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


