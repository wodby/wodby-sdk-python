# ProjectRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Custom role ID; absent for system roles. | [optional] 
**role** | **str** | The system role, or custom. | 
**system** | **bool** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**description** | **str** |  | 
**project_permissions** | **List[str]** |  | 
**env_permissions** | **Dict[str, List[str]]** | Environment permissions by environment type (prod, staging, test, dev, feature). | 
**assignable_to_teams** | **bool** |  | 
**supports_runtime_secret_reveal** | **bool** | Whether memberships with this system role can turn on runtime secret reveal. | 
**membership_count** | **int** | Project memberships holding a custom role. Visible to organization owners, admins and support. | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from wodby.models.project_role import ProjectRole

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectRole from a JSON string
project_role_instance = ProjectRole.from_json(json)
# print the JSON string representation of the object
print(ProjectRole.to_json())

# convert the object into a dict
project_role_dict = project_role_instance.to_dict()
# create an instance of ProjectRole from a dict
project_role_from_dict = ProjectRole.from_dict(project_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


