# AppPreviewPullRequestList

Open pull requests a preview environment can be created for by hand.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configured** | **bool** | True when preview environments are enabled and the base environment exists. | 
**pull_requests** | [**List[AppPreviewPullRequest]**](AppPreviewPullRequest.md) |  | 

## Example

```python
from wodby.models.app_preview_pull_request_list import AppPreviewPullRequestList

# TODO update the JSON string below
json = "{}"
# create an instance of AppPreviewPullRequestList from a JSON string
app_preview_pull_request_list_instance = AppPreviewPullRequestList.from_json(json)
# print the JSON string representation of the object
print(AppPreviewPullRequestList.to_json())

# convert the object into a dict
app_preview_pull_request_list_dict = app_preview_pull_request_list_instance.to_dict()
# create an instance of AppPreviewPullRequestList from a dict
app_preview_pull_request_list_from_dict = AppPreviewPullRequestList.from_dict(app_preview_pull_request_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


