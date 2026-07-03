# StackAutoUpdatePolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**version_policy** | [**StackAutoUpdateVersionPolicy**](StackAutoUpdateVersionPolicy.md) |  | [optional] 

## Example

```python
from wodby.models.stack_auto_update_policy import StackAutoUpdatePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of StackAutoUpdatePolicy from a JSON string
stack_auto_update_policy_instance = StackAutoUpdatePolicy.from_json(json)
# print the JSON string representation of the object
print(StackAutoUpdatePolicy.to_json())

# convert the object into a dict
stack_auto_update_policy_dict = stack_auto_update_policy_instance.to_dict()
# create an instance of StackAutoUpdatePolicy from a dict
stack_auto_update_policy_from_dict = StackAutoUpdatePolicy.from_dict(stack_auto_update_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


