# WorkspaceEligibility200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligible** | **bool** |  | [optional] 
**reasons** | **List[str]** |  | [optional] 
**source_stack_service_id** | **int** |  | [optional] 
**consumer_stack_service_ids** | **List[int]** |  | [optional] 

## Example

```python
from wodby.models.workspace_eligibility200_response import WorkspaceEligibility200Response

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceEligibility200Response from a JSON string
workspace_eligibility200_response_instance = WorkspaceEligibility200Response.from_json(json)
# print the JSON string representation of the object
print(WorkspaceEligibility200Response.to_json())

# convert the object into a dict
workspace_eligibility200_response_dict = workspace_eligibility200_response_instance.to_dict()
# create an instance of WorkspaceEligibility200Response from a dict
workspace_eligibility200_response_from_dict = WorkspaceEligibility200Response.from_dict(workspace_eligibility200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


