# ImportStacksFromGitInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** | Optional for API-key requests; defaults to the API key&#39;s organization. | [optional] 
**project_id** | **int** |  | [optional] 
**integration_id** | **int** |  | 
**remote_git_repo_id** | **str** |  | 
**git_ref** | **str** |  | 
**git_ref_type** | **str** |  | 
**auto_update** | [**GitAutoUpdateSettingsInput**](GitAutoUpdateSettingsInput.md) |  | [optional] 
**available_to_all_projects** | **bool** | Lets every project in the organization use the imported stacks without a project share. Only organization-owned stacks, imported without projectId, can be available to all projects. | [optional] 

## Example

```python
from wodby.models.import_stacks_from_git_input import ImportStacksFromGitInput

# TODO update the JSON string below
json = "{}"
# create an instance of ImportStacksFromGitInput from a JSON string
import_stacks_from_git_input_instance = ImportStacksFromGitInput.from_json(json)
# print the JSON string representation of the object
print(ImportStacksFromGitInput.to_json())

# convert the object into a dict
import_stacks_from_git_input_dict = import_stacks_from_git_input_instance.to_dict()
# create an instance of ImportStacksFromGitInput from a dict
import_stacks_from_git_input_from_dict = ImportStacksFromGitInput.from_dict(import_stacks_from_git_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


