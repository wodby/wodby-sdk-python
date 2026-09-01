# AppEnvironmentCICDSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ci_integration_id** | **int** | CI integration ID. Set to zero to use the built-in Wodby CI service. | 
**registry_integration_id** | **int** | Registry integration ID. Set to zero to use the built-in Wodby registry service. | 

## Example

```python
from wodby.models.app_environment_cicd_settings_input import AppEnvironmentCICDSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironmentCICDSettingsInput from a JSON string
app_environment_cicd_settings_input_instance = AppEnvironmentCICDSettingsInput.from_json(json)
# print the JSON string representation of the object
print(AppEnvironmentCICDSettingsInput.to_json())

# convert the object into a dict
app_environment_cicd_settings_input_dict = app_environment_cicd_settings_input_instance.to_dict()
# create an instance of AppEnvironmentCICDSettingsInput from a dict
app_environment_cicd_settings_input_from_dict = AppEnvironmentCICDSettingsInput.from_dict(app_environment_cicd_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


