# ProjectPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | 
**description** | **str** |  | 
**scope** | **str** |  | 
**always_granted** | **bool** | Every project role grants it, so it cannot be removed from a custom role. | 

## Example

```python
from wodby.models.project_permission import ProjectPermission

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPermission from a JSON string
project_permission_instance = ProjectPermission.from_json(json)
# print the JSON string representation of the object
print(ProjectPermission.to_json())

# convert the object into a dict
project_permission_dict = project_permission_instance.to_dict()
# create an instance of ProjectPermission from a dict
project_permission_from_dict = ProjectPermission.from_dict(project_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


