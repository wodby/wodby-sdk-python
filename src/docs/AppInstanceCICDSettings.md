# AppInstanceCICDSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_instance_id** | **int** |  | 
**ci_integration_id** | **int** | Effective CI integration ID. Zero selects the built-in Wodby CI service. | 
**registry_integration_id** | **int** | Effective registry integration ID. Zero selects the built-in Wodby registry service. | 
**registry_repository** | **str** |  | 

## Example

```python
from wodby.models.app_instance_cicd_settings import AppInstanceCICDSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstanceCICDSettings from a JSON string
app_instance_cicd_settings_instance = AppInstanceCICDSettings.from_json(json)
# print the JSON string representation of the object
print(AppInstanceCICDSettings.to_json())

# convert the object into a dict
app_instance_cicd_settings_dict = app_instance_cicd_settings_instance.to_dict()
# create an instance of AppInstanceCICDSettings from a dict
app_instance_cicd_settings_from_dict = AppInstanceCICDSettings.from_dict(app_instance_cicd_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


