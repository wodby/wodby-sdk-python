# BuildSourceInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_source_type** | **str** |  | 
**boilerplate** | **str** |  | [optional] 
**new_repo_name** | **str** |  | [optional] 
**integration_id** | **int** |  | [optional] 
**remote_git_repo_id** | **str** |  | [optional] 
**git_ref** | **str** |  | [optional] 
**git_ref_type** | **str** |  | [optional] 
**ci_workflow** | **str** |  | [optional] 

## Example

```python
from wodby.models.build_source_input import BuildSourceInput

# TODO update the JSON string below
json = "{}"
# create an instance of BuildSourceInput from a JSON string
build_source_input_instance = BuildSourceInput.from_json(json)
# print the JSON string representation of the object
print(BuildSourceInput.to_json())

# convert the object into a dict
build_source_input_dict = build_source_input_instance.to_dict()
# create an instance of BuildSourceInput from a dict
build_source_input_from_dict = BuildSourceInput.from_dict(build_source_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


