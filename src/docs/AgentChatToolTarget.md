# AgentChatToolTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | What the argument refers to, such as Environment, Project or CI integration. | 
**name** | **str** |  | 
**argument** | **str** | The call&#39;s argument this names, such as project_id. | 

## Example

```python
from wodby.models.agent_chat_tool_target import AgentChatToolTarget

# TODO update the JSON string below
json = "{}"
# create an instance of AgentChatToolTarget from a JSON string
agent_chat_tool_target_instance = AgentChatToolTarget.from_json(json)
# print the JSON string representation of the object
print(AgentChatToolTarget.to_json())

# convert the object into a dict
agent_chat_tool_target_dict = agent_chat_tool_target_instance.to_dict()
# create an instance of AgentChatToolTarget from a dict
agent_chat_tool_target_from_dict = AgentChatToolTarget.from_dict(agent_chat_tool_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


