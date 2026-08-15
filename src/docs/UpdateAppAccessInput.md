# UpdateAppAccessInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**settings** | [**List[AppAccessSettingInput]**](AppAccessSettingInput.md) |  | [optional] 
**endpoints** | [**List[AppAccessEndpointInput]**](AppAccessEndpointInput.md) |  | 

## Example

```python
from wodby.models.update_app_access_input import UpdateAppAccessInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAppAccessInput from a JSON string
update_app_access_input_instance = UpdateAppAccessInput.from_json(json)
# print the JSON string representation of the object
print(UpdateAppAccessInput.to_json())

# convert the object into a dict
update_app_access_input_dict = update_app_access_input_instance.to_dict()
# create an instance of UpdateAppAccessInput from a dict
update_app_access_input_from_dict = UpdateAppAccessInput.from_dict(update_app_access_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


