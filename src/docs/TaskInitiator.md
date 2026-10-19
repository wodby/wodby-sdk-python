# TaskInitiator

Immutable provenance. Client names and versions are self-reported, not verified identities. Contains no credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | 
**user_id** | **int** |  | 
**api_key_id** | **int** |  | [optional] 
**agent_connection_id** | **int** |  | [optional] 
**oauth_client_id** | **str** |  | 
**oauth_client_name** | **str** |  | 
**client_name** | **str** |  | 
**client_version** | **str** |  | 
**tool_name** | **str** |  | 
**request_id** | **str** |  | 

## Example

```python
from wodby.models.task_initiator import TaskInitiator

# TODO update the JSON string below
json = "{}"
# create an instance of TaskInitiator from a JSON string
task_initiator_instance = TaskInitiator.from_json(json)
# print the JSON string representation of the object
print(TaskInitiator.to_json())

# convert the object into a dict
task_initiator_dict = task_initiator_instance.to_dict()
# create an instance of TaskInitiator from a dict
task_initiator_from_dict = TaskInitiator.from_dict(task_initiator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


