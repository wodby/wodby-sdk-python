# AppServiceWorkspaceMount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**path** | **str** | Absolute path in the container. | 
**sub_path** | **str** | Directory of the checkout that is mounted; empty for the whole repository. | 
**read_only** | **bool** |  | 

## Example

```python
from wodby.models.app_service_workspace_mount import AppServiceWorkspaceMount

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceWorkspaceMount from a JSON string
app_service_workspace_mount_instance = AppServiceWorkspaceMount.from_json(json)
# print the JSON string representation of the object
print(AppServiceWorkspaceMount.to_json())

# convert the object into a dict
app_service_workspace_mount_dict = app_service_workspace_mount_instance.to_dict()
# create an instance of AppServiceWorkspaceMount from a dict
app_service_workspace_mount_from_dict = AppServiceWorkspaceMount.from_dict(app_service_workspace_mount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


