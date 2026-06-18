# NewProjectInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** | Optional for API-key requests; defaults to the API key&#39;s organization. | [optional] 
**name** | **str** |  | 
**title** | **str** |  | 
**team_ids** | **List[int]** |  | [optional] 
**org_membership_ids** | **List[int]** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from wodby.models.new_project_input import NewProjectInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewProjectInput from a JSON string
new_project_input_instance = NewProjectInput.from_json(json)
# print the JSON string representation of the object
print(NewProjectInput.to_json())

# convert the object into a dict
new_project_input_dict = new_project_input_instance.to_dict()
# create an instance of NewProjectInput from a dict
new_project_input_from_dict = NewProjectInput.from_dict(new_project_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


