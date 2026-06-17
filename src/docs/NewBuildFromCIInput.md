# NewBuildFromCIInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_service_id** | **int** |  | 
**git_commit_sha** | **str** |  | 
**git_ref** | **str** |  | 
**git_ref_type** | **str** |  | 
**build_num** | **int** |  | 
**build_id** | **str** |  | 
**workflow** | **str** |  | [optional] 
**git_commit_author_name** | **str** |  | [optional] 
**git_commit_author_email** | **str** |  | [optional] 
**git_commit_message** | **str** |  | [optional] 
**provider** | **str** |  | 
**post_deployment** | **str** |  | [optional] 

## Example

```python
from wodby.models.new_build_from_ci_input import NewBuildFromCIInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewBuildFromCIInput from a JSON string
new_build_from_ci_input_instance = NewBuildFromCIInput.from_json(json)
# print the JSON string representation of the object
print(NewBuildFromCIInput.to_json())

# convert the object into a dict
new_build_from_ci_input_dict = new_build_from_ci_input_instance.to_dict()
# create an instance of NewBuildFromCIInput from a dict
new_build_from_ci_input_from_dict = NewBuildFromCIInput.from_dict(new_build_from_ci_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


