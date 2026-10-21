# AgentChatApprovalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **int** | The tool message that waits for approval. | 
**approve** | **bool** |  | 

## Example

```python
from wodby.models.agent_chat_approval_request import AgentChatApprovalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentChatApprovalRequest from a JSON string
agent_chat_approval_request_instance = AgentChatApprovalRequest.from_json(json)
# print the JSON string representation of the object
print(AgentChatApprovalRequest.to_json())

# convert the object into a dict
agent_chat_approval_request_dict = agent_chat_approval_request_instance.to_dict()
# create an instance of AgentChatApprovalRequest from a dict
agent_chat_approval_request_from_dict = AgentChatApprovalRequest.from_dict(agent_chat_approval_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


