# AgentChat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**org_id** | **int** |  | 
**title** | **str** |  | 
**status** | **str** | idle takes a message; running is the agent working; waiting is a call that waits for approval or an answer. | 
**error** | **str** | Why the last run stopped without an answer, or empty. | 
**approval_mode** | [**AgentChatApprovalMode**](AgentChatApprovalMode.md) |  | 
**context_tokens** | **int** | Tokens in the chat&#39;s context after the newest reply. | 
**context_limit** | **int** | Context size at which the agent summarizes the chat to continue it. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.agent_chat import AgentChat

# TODO update the JSON string below
json = "{}"
# create an instance of AgentChat from a JSON string
agent_chat_instance = AgentChat.from_json(json)
# print the JSON string representation of the object
print(AgentChat.to_json())

# convert the object into a dict
agent_chat_dict = agent_chat_instance.to_dict()
# create an instance of AgentChat from a dict
agent_chat_from_dict = AgentChat.from_dict(agent_chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


