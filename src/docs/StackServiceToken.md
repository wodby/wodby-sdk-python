# StackServiceToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**stack_service_id** | **int** |  | 
**name** | **str** |  | 
**value** | **str** |  | [optional] 
**regex** | **str** |  | [optional] 
**value_secret_id** | **int** |  | [optional] 
**env_type** | **str** |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from wodby.models.stack_service_token import StackServiceToken

# TODO update the JSON string below
json = "{}"
# create an instance of StackServiceToken from a JSON string
stack_service_token_instance = StackServiceToken.from_json(json)
# print the JSON string representation of the object
print(StackServiceToken.to_json())

# convert the object into a dict
stack_service_token_dict = stack_service_token_instance.to_dict()
# create an instance of StackServiceToken from a dict
stack_service_token_from_dict = StackServiceToken.from_dict(stack_service_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


