# ProjectRoleInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** | Used when creating a role. Optional for API-key requests; defaults to the API key&#39;s organization. | [optional] 
**name** | **str** | Lowercase letters, digits, dashes or underscores; unique in the organization. | 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**project_permissions** | **List[str]** |  | 
**env_permissions** | **Dict[str, List[str]]** | Environment permissions by environment type (prod, staging, test, dev, feature). | 

## Example

```python
from wodby.models.project_role_input import ProjectRoleInput

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectRoleInput from a JSON string
project_role_input_instance = ProjectRoleInput.from_json(json)
# print the JSON string representation of the object
print(ProjectRoleInput.to_json())

# convert the object into a dict
project_role_input_dict = project_role_input_instance.to_dict()
# create an instance of ProjectRoleInput from a dict
project_role_input_from_dict = ProjectRoleInput.from_dict(project_role_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


