# NewStackInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** | Optional for API-key requests; defaults to the API key&#39;s organization. | [optional] 
**project_id** | **int** |  | [optional] 
**available_to_all_projects** | **bool** | Lets every project in the organization use the new resource without a project share. Only an organization-owned resource, created without projectId, can be available to all projects. | [optional] 
**name** | **str** |  | 
**title** | **str** |  | 
**icon** | **str** |  | [optional] 
**services** | [**List[NewStackServiceDefinitionInput]**](NewStackServiceDefinitionInput.md) |  | 

## Example

```python
from wodby.models.new_stack_input import NewStackInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewStackInput from a JSON string
new_stack_input_instance = NewStackInput.from_json(json)
# print the JSON string representation of the object
print(NewStackInput.to_json())

# convert the object into a dict
new_stack_input_dict = new_stack_input_instance.to_dict()
# create an instance of NewStackInput from a dict
new_stack_input_from_dict = NewStackInput.from_dict(new_stack_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


