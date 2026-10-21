# AgentChatApprovalModeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_mode** | [**AgentChatApprovalMode**](AgentChatApprovalMode.md) |  | 

## Example

```python
from wodby.models.agent_chat_approval_mode_request import AgentChatApprovalModeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentChatApprovalModeRequest from a JSON string
agent_chat_approval_mode_request_instance = AgentChatApprovalModeRequest.from_json(json)
# print the JSON string representation of the object
print(AgentChatApprovalModeRequest.to_json())

# convert the object into a dict
agent_chat_approval_mode_request_dict = agent_chat_approval_mode_request_instance.to_dict()
# create an instance of AgentChatApprovalModeRequest from a dict
agent_chat_approval_mode_request_from_dict = AgentChatApprovalModeRequest.from_dict(agent_chat_approval_mode_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


