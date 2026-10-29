# NewAppPreviewEnvironmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | Pull request number. | 
**remote_git_repo_id** | **str** | Remote repository of the pull request. Required when the base environment tracks several repositories. | [optional] 

## Example

```python
from wodby.models.new_app_preview_environment_request import NewAppPreviewEnvironmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NewAppPreviewEnvironmentRequest from a JSON string
new_app_preview_environment_request_instance = NewAppPreviewEnvironmentRequest.from_json(json)
# print the JSON string representation of the object
print(NewAppPreviewEnvironmentRequest.to_json())

# convert the object into a dict
new_app_preview_environment_request_dict = new_app_preview_environment_request_instance.to_dict()
# create an instance of NewAppPreviewEnvironmentRequest from a dict
new_app_preview_environment_request_from_dict = NewAppPreviewEnvironmentRequest.from_dict(new_app_preview_environment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


