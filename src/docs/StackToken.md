# StackToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**value** | **str** | Omitted for secret values. | [optional] 
**value_secret_id** | **int** |  | [optional] 
**regex** | **str** |  | [optional] 
**env_type** | **str** | Limit the value to app environments of this type. | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from wodby.models.stack_token import StackToken

# TODO update the JSON string below
json = "{}"
# create an instance of StackToken from a JSON string
stack_token_instance = StackToken.from_json(json)
# print the JSON string representation of the object
print(StackToken.to_json())

# convert the object into a dict
stack_token_dict = stack_token_instance.to_dict()
# create an instance of StackToken from a dict
stack_token_from_dict = StackToken.from_dict(stack_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


