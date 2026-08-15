# ValidateAppAccessHostnameInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**List[AppAccessSettingInput]**](AppAccessSettingInput.md) |  | [optional] 
**host** | **str** |  | 

## Example

```python
from wodby.models.validate_app_access_hostname_input import ValidateAppAccessHostnameInput

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateAppAccessHostnameInput from a JSON string
validate_app_access_hostname_input_instance = ValidateAppAccessHostnameInput.from_json(json)
# print the JSON string representation of the object
print(ValidateAppAccessHostnameInput.to_json())

# convert the object into a dict
validate_app_access_hostname_input_dict = validate_app_access_hostname_input_instance.to_dict()
# create an instance of ValidateAppAccessHostnameInput from a dict
validate_app_access_hostname_input_from_dict = ValidateAppAccessHostnameInput.from_dict(validate_app_access_hostname_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


