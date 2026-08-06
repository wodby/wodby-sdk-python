# AppInstanceCICDSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ci_integration_id** | **int** | CI integration ID. Set to zero to use the built-in Wodby CI service. | 
**registry_integration_id** | **int** | Registry integration ID. Set to zero to use the built-in Wodby registry service. | 

## Example

```python
from wodby.models.app_instance_cicd_settings_input import AppInstanceCICDSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstanceCICDSettingsInput from a JSON string
app_instance_cicd_settings_input_instance = AppInstanceCICDSettingsInput.from_json(json)
# print the JSON string representation of the object
print(AppInstanceCICDSettingsInput.to_json())

# convert the object into a dict
app_instance_cicd_settings_input_dict = app_instance_cicd_settings_input_instance.to_dict()
# create an instance of AppInstanceCICDSettingsInput from a dict
app_instance_cicd_settings_input_from_dict = AppInstanceCICDSettingsInput.from_dict(app_instance_cicd_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


