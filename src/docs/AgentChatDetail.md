# AgentChatDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**AgentChat**](AgentChat.md) |  | 
**messages** | [**List[AgentChatMessage]**](AgentChatMessage.md) |  | 

## Example

```python
from wodby.models.agent_chat_detail import AgentChatDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AgentChatDetail from a JSON string
agent_chat_detail_instance = AgentChatDetail.from_json(json)
# print the JSON string representation of the object
print(AgentChatDetail.to_json())

# convert the object into a dict
agent_chat_detail_dict = agent_chat_detail_instance.to_dict()
# create an instance of AgentChatDetail from a dict
agent_chat_detail_from_dict = AgentChatDetail.from_dict(agent_chat_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


