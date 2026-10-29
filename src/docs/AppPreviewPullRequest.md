# AppPreviewPullRequest

An open pull request into the branch the preview base environment tracks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** |  | 
**title** | **str** |  | 
**url** | **str** |  | 
**remote_git_repo_id** | **str** | Remote repository of the pull request. Pass it when creating the preview environment. | 
**repository_url** | **str** |  | 
**head_ref** | **str** |  | 
**base_ref** | **str** |  | 
**author** | **str** |  | 
**draft** | **bool** |  | 
**from_fork** | **bool** | The head branch lives in another repository. Pull requests from forks never get preview environments. | 
**updated_at** | **datetime** |  | [optional] 
**has_preview** | **bool** | The pull request already has a preview environment, possibly one being deleted. | 
**preview_app_environment_id** | **int** |  | [optional] 
**skip_reason** | **str** | Why a preview environment cannot be created for this pull request now. Null when it can. | [optional] 

## Example

```python
from wodby.models.app_preview_pull_request import AppPreviewPullRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppPreviewPullRequest from a JSON string
app_preview_pull_request_instance = AppPreviewPullRequest.from_json(json)
# print the JSON string representation of the object
print(AppPreviewPullRequest.to_json())

# convert the object into a dict
app_preview_pull_request_dict = app_preview_pull_request_instance.to_dict()
# create an instance of AppPreviewPullRequest from a dict
app_preview_pull_request_from_dict = AppPreviewPullRequest.from_dict(app_preview_pull_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


