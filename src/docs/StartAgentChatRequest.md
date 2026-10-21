# StartAgentChatRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** | Optional for API-key requests; defaults to the API key&#39;s organization. | [optional] 
**message** | **str** |  | 
**approval_mode** | [**AgentChatApprovalMode**](AgentChatApprovalMode.md) | Optional; without it, the chat asks before every change. | [optional] 

## Example

```python
from wodby.models.start_agent_chat_request import StartAgentChatRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartAgentChatRequest from a JSON string
start_agent_chat_request_instance = StartAgentChatRequest.from_json(json)
# print the JSON string representation of the object
print(StartAgentChatRequest.to_json())

# convert the object into a dict
start_agent_chat_request_dict = start_agent_chat_request_instance.to_dict()
# create an instance of StartAgentChatRequest from a dict
start_agent_chat_request_from_dict = StartAgentChatRequest.from_dict(start_agent_chat_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


