# AppEnvironmentDeploymentSettings

Defaults for the environment's deployments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_scripts_for_older_builds** | **bool** | Run repository pre- and post-deployment scripts when a deployment rolls an app service back to an older build. | 
**skip_rollback** | **bool** | Keep a failed rollout in place instead of restoring the previous release, for every deployment. | 

## Example

```python
from wodby.models.app_environment_deployment_settings import AppEnvironmentDeploymentSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironmentDeploymentSettings from a JSON string
app_environment_deployment_settings_instance = AppEnvironmentDeploymentSettings.from_json(json)
# print the JSON string representation of the object
print(AppEnvironmentDeploymentSettings.to_json())

# convert the object into a dict
app_environment_deployment_settings_dict = app_environment_deployment_settings_instance.to_dict()
# create an instance of AppEnvironmentDeploymentSettings from a dict
app_environment_deployment_settings_from_dict = AppEnvironmentDeploymentSettings.from_dict(app_environment_deployment_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


