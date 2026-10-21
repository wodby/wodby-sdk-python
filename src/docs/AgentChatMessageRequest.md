# AgentChatMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from wodby.models.agent_chat_message_request import AgentChatMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentChatMessageRequest from a JSON string
agent_chat_message_request_instance = AgentChatMessageRequest.from_json(json)
# print the JSON string representation of the object
print(AgentChatMessageRequest.to_json())

# convert the object into a dict
agent_chat_message_request_dict = agent_chat_message_request_instance.to_dict()
# create an instance of AgentChatMessageRequest from a dict
agent_chat_message_request_from_dict = AgentChatMessageRequest.from_dict(agent_chat_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


