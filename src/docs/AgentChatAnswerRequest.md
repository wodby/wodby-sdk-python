# AgentChatAnswerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **int** | The ask_user message that waits for an answer. | 
**answers** | **List[str]** |  | 

## Example

```python
from wodby.models.agent_chat_answer_request import AgentChatAnswerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentChatAnswerRequest from a JSON string
agent_chat_answer_request_instance = AgentChatAnswerRequest.from_json(json)
# print the JSON string representation of the object
print(AgentChatAnswerRequest.to_json())

# convert the object into a dict
agent_chat_answer_request_dict = agent_chat_answer_request_instance.to_dict()
# create an instance of AgentChatAnswerRequest from a dict
agent_chat_answer_request_from_dict = AgentChatAnswerRequest.from_dict(agent_chat_answer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


