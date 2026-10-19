# ProjectShareInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**access** | **str** |  | 

## Example

```python
from wodby.models.project_share_input import ProjectShareInput

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectShareInput from a JSON string
project_share_input_instance = ProjectShareInput.from_json(json)
# print the JSON string representation of the object
print(ProjectShareInput.to_json())

# convert the object into a dict
project_share_input_dict = project_share_input_instance.to_dict()
# create an instance of ProjectShareInput from a dict
project_share_input_from_dict = ProjectShareInput.from_dict(project_share_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


