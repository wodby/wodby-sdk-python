# AppEnvironmentPermissions

What the caller can do in the app environment, from their organization role and project role. Returned by getAppEnvironment and getAppEnvironmentByName only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploy** | **bool** |  | 
**operate** | **bool** |  | 
**configure** | **bool** |  | 
**upgrade** | **bool** |  | 
**shell** | **bool** |  | 
**backup** | **bool** |  | 
**restore** | **bool** |  | 
**delete** | **bool** |  | 

## Example

```python
from wodby.models.app_environment_permissions import AppEnvironmentPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironmentPermissions from a JSON string
app_environment_permissions_instance = AppEnvironmentPermissions.from_json(json)
# print the JSON string representation of the object
print(AppEnvironmentPermissions.to_json())

# convert the object into a dict
app_environment_permissions_dict = app_environment_permissions_instance.to_dict()
# create an instance of AppEnvironmentPermissions from a dict
app_environment_permissions_from_dict = AppEnvironmentPermissions.from_dict(app_environment_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


