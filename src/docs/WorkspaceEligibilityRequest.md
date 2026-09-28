# WorkspaceEligibilityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stack_rev_id** | **int** |  | 
**cluster_id** | **int** |  | [optional] 
**disabled_service_ids** | **List[int]** |  | 

## Example

```python
from wodby.models.workspace_eligibility_request import WorkspaceEligibilityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceEligibilityRequest from a JSON string
workspace_eligibility_request_instance = WorkspaceEligibilityRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceEligibilityRequest.to_json())

# convert the object into a dict
workspace_eligibility_request_dict = workspace_eligibility_request_instance.to_dict()
# create an instance of WorkspaceEligibilityRequest from a dict
workspace_eligibility_request_from_dict = WorkspaceEligibilityRequest.from_dict(workspace_eligibility_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


