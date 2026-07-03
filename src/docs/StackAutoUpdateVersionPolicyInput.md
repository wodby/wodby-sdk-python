# StackAutoUpdateVersionPolicyInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | [optional] 
**allow_patch** | **bool** |  | [optional] 
**allow_minor** | **bool** |  | [optional] 
**allow_major** | **bool** |  | [optional] 

## Example

```python
from wodby.models.stack_auto_update_version_policy_input import StackAutoUpdateVersionPolicyInput

# TODO update the JSON string below
json = "{}"
# create an instance of StackAutoUpdateVersionPolicyInput from a JSON string
stack_auto_update_version_policy_input_instance = StackAutoUpdateVersionPolicyInput.from_json(json)
# print the JSON string representation of the object
print(StackAutoUpdateVersionPolicyInput.to_json())

# convert the object into a dict
stack_auto_update_version_policy_input_dict = stack_auto_update_version_policy_input_instance.to_dict()
# create an instance of StackAutoUpdateVersionPolicyInput from a dict
stack_auto_update_version_policy_input_from_dict = StackAutoUpdateVersionPolicyInput.from_dict(stack_auto_update_version_policy_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


