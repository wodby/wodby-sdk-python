# StackAutoOriginUpdateVersionPolicyInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | [optional] 
**allow_patch** | **bool** |  | [optional] 
**allow_minor** | **bool** |  | [optional] 
**allow_major** | **bool** |  | [optional] 

## Example

```python
from wodby.models.stack_auto_origin_update_version_policy_input import StackAutoOriginUpdateVersionPolicyInput

# TODO update the JSON string below
json = "{}"
# create an instance of StackAutoOriginUpdateVersionPolicyInput from a JSON string
stack_auto_origin_update_version_policy_input_instance = StackAutoOriginUpdateVersionPolicyInput.from_json(json)
# print the JSON string representation of the object
print(StackAutoOriginUpdateVersionPolicyInput.to_json())

# convert the object into a dict
stack_auto_origin_update_version_policy_input_dict = stack_auto_origin_update_version_policy_input_instance.to_dict()
# create an instance of StackAutoOriginUpdateVersionPolicyInput from a dict
stack_auto_origin_update_version_policy_input_from_dict = StackAutoOriginUpdateVersionPolicyInput.from_dict(stack_auto_origin_update_version_policy_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


