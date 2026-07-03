# StackAutoUpdatePolicyInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | [optional] 
**version_policy** | [**StackAutoUpdateVersionPolicyInput**](StackAutoUpdateVersionPolicyInput.md) |  | [optional] 

## Example

```python
from wodby.models.stack_auto_update_policy_input import StackAutoUpdatePolicyInput

# TODO update the JSON string below
json = "{}"
# create an instance of StackAutoUpdatePolicyInput from a JSON string
stack_auto_update_policy_input_instance = StackAutoUpdatePolicyInput.from_json(json)
# print the JSON string representation of the object
print(StackAutoUpdatePolicyInput.to_json())

# convert the object into a dict
stack_auto_update_policy_input_dict = stack_auto_update_policy_input_instance.to_dict()
# create an instance of StackAutoUpdatePolicyInput from a dict
stack_auto_update_policy_input_from_dict = StackAutoUpdatePolicyInput.from_dict(stack_auto_update_policy_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


