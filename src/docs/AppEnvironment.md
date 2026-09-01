# AppEnvironment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**environment_type** | **str** |  | 
**status** | **str** |  | 
**outdated** | **bool** |  | 
**main_domain** | **str** |  | [optional] 
**main_route_cert** | [**AppEnvironmentMainRouteCert**](AppEnvironmentMainRouteCert.md) |  | 
**app_id** | **int** |  | 
**cluster_id** | **int** |  | 
**stack_id** | **int** |  | 
**stack_rev_id** | **int** |  | 
**stack_name** | **str** |  | 
**stack_title** | **str** |  | 
**stack_icon** | **str** |  | 
**stack_rev_number** | **int** |  | 
**stack_version** | **str** |  | 
**access** | [**AppAccess**](AppAccess.md) |  | [optional] 
**routing_mode** | **str** |  | 
**routing_pending** | **bool** |  | 
**maintenance_mode** | **bool** |  | 
**maintenance_mode_active** | **bool** |  | 
**configuration_ready** | **bool** |  | 
**configuration_issues** | [**List[AppServiceConfigurationIssue]**](AppServiceConfigurationIssue.md) |  | 
**settings** | [**AppEnvironmentSettings**](AppEnvironmentSettings.md) |  | [optional] 
**health** | [**AppEnvironmentHealth**](AppEnvironmentHealth.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.app_environment import AppEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironment from a JSON string
app_environment_instance = AppEnvironment.from_json(json)
# print the JSON string representation of the object
print(AppEnvironment.to_json())

# convert the object into a dict
app_environment_dict = app_environment_instance.to_dict()
# create an instance of AppEnvironment from a dict
app_environment_from_dict = AppEnvironment.from_dict(app_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


