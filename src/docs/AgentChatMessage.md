# AgentChatMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**role** | **str** | A tool message is a call&#39;s result, or a call that waits; a summary replaced earlier messages for the model. | 
**content** | **str** |  | 
**tool** | **str** | For a tool message, the Wodby tool the call is for. ask_user is a question from the agent. | [optional] 
**tool_arguments** | **Dict[str, object]** | For a tool message, the call&#39;s arguments. For ask_user, the question, its options (label, description, recommended) and whether several may be chosen. The recommended options come first and their labels end with (Recommended). | [optional] 
**approval** | **str** | Set on a call that changes something or asks a question. | 
**tool_destructive** | **bool** | True for a call that deletes, overwrites, upgrades or interrupts something, or runs a command in a container. | 
**tool_targets** | [**List[AgentChatToolTarget]**](AgentChatToolTarget.md) | For a call that waits for approval, what its ID arguments refer to, as far as the user may see them, each with the argument it names. | 
**is_error** | **bool** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from wodby.models.agent_chat_message import AgentChatMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AgentChatMessage from a JSON string
agent_chat_message_instance = AgentChatMessage.from_json(json)
# print the JSON string representation of the object
print(AgentChatMessage.to_json())

# convert the object into a dict
agent_chat_message_dict = agent_chat_message_instance.to_dict()
# create an instance of AgentChatMessage from a dict
agent_chat_message_from_dict = AgentChatMessage.from_dict(agent_chat_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


