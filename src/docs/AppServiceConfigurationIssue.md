# AppServiceConfigurationIssue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_service_id** | **int** |  | 
**app_service_name** | **str** |  | 
**app_service_title** | **str** |  | 
**code** | **str** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from wodby.models.app_service_configuration_issue import AppServiceConfigurationIssue

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceConfigurationIssue from a JSON string
app_service_configuration_issue_instance = AppServiceConfigurationIssue.from_json(json)
# print the JSON string representation of the object
print(AppServiceConfigurationIssue.to_json())

# convert the object into a dict
app_service_configuration_issue_dict = app_service_configuration_issue_instance.to_dict()
# create an instance of AppServiceConfigurationIssue from a dict
app_service_configuration_issue_from_dict = AppServiceConfigurationIssue.from_dict(app_service_configuration_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


