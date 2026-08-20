# ImportServicesFromGitInput


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
**registry_integration_id** | **int** | Optional registry integration used when an imported service image requires authentication. | [optional] 

## Example

```python
from wodby.models.import_services_from_git_input import ImportServicesFromGitInput

# TODO update the JSON string below
json = "{}"
# create an instance of ImportServicesFromGitInput from a JSON string
import_services_from_git_input_instance = ImportServicesFromGitInput.from_json(json)
# print the JSON string representation of the object
print(ImportServicesFromGitInput.to_json())

# convert the object into a dict
import_services_from_git_input_dict = import_services_from_git_input_instance.to_dict()
# create an instance of ImportServicesFromGitInput from a dict
import_services_from_git_input_from_dict = ImportServicesFromGitInput.from_dict(import_services_from_git_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


