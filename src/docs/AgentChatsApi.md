# wodby.AgentChatsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**answer_agent_chat_approval**](AgentChatsApi.md#answer_agent_chat_approval) | **POST** /agent-chats/{id}/approvals | Approve or decline agent change
[**answer_agent_chat_question**](AgentChatsApi.md#answer_agent_chat_question) | **POST** /agent-chats/{id}/answers | Answer agent question
[**delete_agent_chat**](AgentChatsApi.md#delete_agent_chat) | **DELETE** /agent-chats/{id} | Delete agent chat
[**get_agent_chat**](AgentChatsApi.md#get_agent_chat) | **GET** /agent-chats/{id} | Get agent chat
[**list_agent_chats**](AgentChatsApi.md#list_agent_chats) | **GET** /agent-chats | List agent chats
[**send_agent_chat_message**](AgentChatsApi.md#send_agent_chat_message) | **POST** /agent-chats/{id}/messages | Send agent chat message
[**start_agent_chat**](AgentChatsApi.md#start_agent_chat) | **POST** /agent-chats | Start agent chat
[**stop_agent_chat**](AgentChatsApi.md#stop_agent_chat) | **POST** /agent-chats/{id}/stop | Stop agent chat
[**update_agent_chat_approval_mode**](AgentChatsApi.md#update_agent_chat_approval_mode) | **PUT** /agent-chats/{id}/approval-mode | Set agent chat approval mode


# **answer_agent_chat_approval**
> AgentChat answer_agent_chat_approval(id, agent_chat_approval_request, org_id=org_id)

Approve or decline agent change

Approves or declines a tool call that waits for approval. The run continues once nothing waits any more. Approving a destructive call, marked toolDestructive, lets it delete, overwrite, upgrade or interrupt what its arguments name.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.agent_chat import AgentChat
from wodby.models.agent_chat_approval_request import AgentChatApprovalRequest
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.AgentChatsApi(api_client)
    id = 56 # int | 
    agent_chat_approval_request = wodby.AgentChatApprovalRequest() # AgentChatApprovalRequest | 
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)

    try:
        # Approve or decline agent change
        api_response = api_instance.answer_agent_chat_approval(id, agent_chat_approval_request, org_id=org_id)
        print("The response of AgentChatsApi->answer_agent_chat_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentChatsApi->answer_agent_chat_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **agent_chat_approval_request** | [**AgentChatApprovalRequest**](AgentChatApprovalRequest.md)|  | 
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 

### Return type

[**AgentChat**](AgentChat.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent chat |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **answer_agent_chat_question**
> AgentChat answer_agent_chat_question(id, agent_chat_answer_request, org_id=org_id)

Answer agent question

Answers a question the agent asked with the tool ask_user, with option labels from its arguments or other text. The run continues once nothing waits any more.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.agent_chat import AgentChat
from wodby.models.agent_chat_answer_request import AgentChatAnswerRequest
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.AgentChatsApi(api_client)
    id = 56 # int | 
    agent_chat_answer_request = wodby.AgentChatAnswerRequest() # AgentChatAnswerRequest | 
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)

    try:
        # Answer agent question
        api_response = api_instance.answer_agent_chat_question(id, agent_chat_answer_request, org_id=org_id)
        print("The response of AgentChatsApi->answer_agent_chat_question:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentChatsApi->answer_agent_chat_question: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **agent_chat_answer_request** | [**AgentChatAnswerRequest**](AgentChatAnswerRequest.md)|  | 
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 

### Return type

[**AgentChat**](AgentChat.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent chat |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_chat**
> OperationResult delete_agent_chat(id, org_id=org_id)

Delete agent chat

Deletes a chat and its messages. It does not undo what the agent did.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.operation_result import OperationResult
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.AgentChatsApi(api_client)
    id = 56 # int | 
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)

    try:
        # Delete agent chat
        api_response = api_instance.delete_agent_chat(id, org_id=org_id)
        print("The response of AgentChatsApi->delete_agent_chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentChatsApi->delete_agent_chat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_chat**
> AgentChatDetail get_agent_chat(id, org_id=org_id)

Get agent chat

Returns a chat with its messages. A tool message with approval pending is a change that waits for approval, or, for the tool ask_user, a question that waits for an answer.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.agent_chat_detail import AgentChatDetail
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.AgentChatsApi(api_client)
    id = 56 # int | 
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)

    try:
        # Get agent chat
        api_response = api_instance.get_agent_chat(id, org_id=org_id)
        print("The response of AgentChatsApi->get_agent_chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentChatsApi->get_agent_chat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 

### Return type

[**AgentChatDetail**](AgentChatDetail.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent chat with its messages |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_agent_chats**
> List[AgentChat] list_agent_chats(org_id=org_id)

List agent chats

Returns the API key user's chats with Wodby Agent in the organization, the most recently active first.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.agent_chat import AgentChat
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.AgentChatsApi(api_client)
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)

    try:
        # List agent chats
        api_response = api_instance.list_agent_chats(org_id=org_id)
        print("The response of AgentChatsApi->list_agent_chats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentChatsApi->list_agent_chats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 

### Return type

[**List[AgentChat]**](AgentChat.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent chats |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_agent_chat_message**
> AgentChat send_agent_chat_message(id, agent_chat_message_request, org_id=org_id)

Send agent chat message

Adds a message to an idle chat and starts the agent's run, which continues after the response.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.agent_chat import AgentChat
from wodby.models.agent_chat_message_request import AgentChatMessageRequest
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.AgentChatsApi(api_client)
    id = 56 # int | 
    agent_chat_message_request = wodby.AgentChatMessageRequest() # AgentChatMessageRequest | 
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)

    try:
        # Send agent chat message
        api_response = api_instance.send_agent_chat_message(id, agent_chat_message_request, org_id=org_id)
        print("The response of AgentChatsApi->send_agent_chat_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentChatsApi->send_agent_chat_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **agent_chat_message_request** | [**AgentChatMessageRequest**](AgentChatMessageRequest.md)|  | 
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 

### Return type

[**AgentChat**](AgentChat.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent chat |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_agent_chat**
> AgentChat start_agent_chat(start_agent_chat_request)

Start agent chat

Starts a chat with Wodby Agent with its first message. The agent's run continues after the response: read the chat until its status is idle, or waiting for an approval or an answer. Each run uses the organization's AI credits.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.agent_chat import AgentChat
from wodby.models.start_agent_chat_request import StartAgentChatRequest
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.AgentChatsApi(api_client)
    start_agent_chat_request = wodby.StartAgentChatRequest() # StartAgentChatRequest | 

    try:
        # Start agent chat
        api_response = api_instance.start_agent_chat(start_agent_chat_request)
        print("The response of AgentChatsApi->start_agent_chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentChatsApi->start_agent_chat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_agent_chat_request** | [**StartAgentChatRequest**](StartAgentChatRequest.md)|  | 

### Return type

[**AgentChat**](AgentChat.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Started agent chat |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_agent_chat**
> AgentChat stop_agent_chat(id, org_id=org_id)

Stop agent chat

Stops the chat's run and declines the calls that wait for approval. A chat without a run is returned as it is.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.agent_chat import AgentChat
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.AgentChatsApi(api_client)
    id = 56 # int | 
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)

    try:
        # Stop agent chat
        api_response = api_instance.stop_agent_chat(id, org_id=org_id)
        print("The response of AgentChatsApi->stop_agent_chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentChatsApi->stop_agent_chat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 

### Return type

[**AgentChat**](AgentChat.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent chat |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_chat_approval_mode**
> AgentChat update_agent_chat_approval_mode(id, agent_chat_approval_mode_request, org_id=org_id)

Set agent chat approval mode

Sets whether the chat asks before a change. A run that is going on follows the new mode from its next step; calls that already wait for approval keep waiting for an answer.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.agent_chat import AgentChat
from wodby.models.agent_chat_approval_mode_request import AgentChatApprovalModeRequest
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.AgentChatsApi(api_client)
    id = 56 # int | 
    agent_chat_approval_mode_request = wodby.AgentChatApprovalModeRequest() # AgentChatApprovalModeRequest | 
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)

    try:
        # Set agent chat approval mode
        api_response = api_instance.update_agent_chat_approval_mode(id, agent_chat_approval_mode_request, org_id=org_id)
        print("The response of AgentChatsApi->update_agent_chat_approval_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentChatsApi->update_agent_chat_approval_mode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **agent_chat_approval_mode_request** | [**AgentChatApprovalModeRequest**](AgentChatApprovalModeRequest.md)|  | 
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 

### Return type

[**AgentChat**](AgentChat.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent chat |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

