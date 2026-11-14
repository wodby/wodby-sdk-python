# AppService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**type** | **str** |  | 
**status** | **str** |  | 
**replicas** | **int** |  | 
**scalability** | [**AppServiceScalability**](AppServiceScalability.md) |  | [optional] 
**version** | **str** |  | 
**main** | **bool** |  | 
**disabled** | **bool** |  | 
**external** | **bool** |  | 
**required** | **bool** |  | 
**needs_rebuild** | **bool** |  | 
**needs_redeploy** | **bool** |  | 
**stack_state** | **str** |  | 
**configuration_ready** | **bool** |  | 
**build_source_boilerplate** | **str** |  | [optional] 
**ci_policy** | **str** |  | 
**effective_ci_integration_id** | **int** |  | [optional] 
**configuration_issues** | [**List[AppServiceConfigurationIssue]**](AppServiceConfigurationIssue.md) |  | 
**app_instance_id** | **int** |  | 
**service_rev_id** | **int** |  | 
**parent_app_service_id** | **int** |  | [optional] 
**deployment_configuration** | [**ServiceDeploymentConfiguration**](ServiceDeploymentConfiguration.md) |  | 
**icon** | **str** |  | [optional] 
**eol** | **bool** | True when the app service&#39;s version has reached its end of life. | [optional] 
**build_source_type** | **str** | How the app service gets its source code to build, public, clone or connect. Null when it is not built from source. | [optional] 
**derivative** | **str** | The service derivative the app service runs. Null for the service itself. | [optional] 
**git_repo_id** | **int** |  | [optional] 
**workspace_mounts** | [**List[AppServiceWorkspaceMount]**](AppServiceWorkspaceMount.md) | Workspace code mounts of the service, with its settings resolved in the paths. Empty without a workspace contract. | [optional] 
**database_db_id** | **int** | The database the app service uses on a provider-managed database server. | [optional] 
**database_user_id** | **int** | The database user the app service connects as on a provider-managed database server. | [optional] 
**customizations** | [**List[AppServiceCustomization]**](AppServiceCustomization.md) | What this app environment set differently from the stack service the app service was created from, such as a setting value, an extra variable or another link target. Only names are returned, never values. Returned only by GET /app-services/{id}. | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.app_service import AppService

# TODO update the JSON string below
json = "{}"
# create an instance of AppService from a JSON string
app_service_instance = AppService.from_json(json)
# print the JSON string representation of the object
print(AppService.to_json())

# convert the object into a dict
app_service_dict = app_service_instance.to_dict()
# create an instance of AppService from a dict
app_service_from_dict = AppService.from_dict(app_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


