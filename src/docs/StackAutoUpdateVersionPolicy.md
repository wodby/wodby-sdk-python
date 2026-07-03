# StackAutoUpdateVersionPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | 
**allow_patch** | **bool** |  | 
**allow_minor** | **bool** |  | 
**allow_major** | **bool** |  | 

## Example

```python
from wodby.models.stack_auto_update_version_policy import StackAutoUpdateVersionPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of StackAutoUpdateVersionPolicy from a JSON string
stack_auto_update_version_policy_instance = StackAutoUpdateVersionPolicy.from_json(json)
# print the JSON string representation of the object
print(StackAutoUpdateVersionPolicy.to_json())

# convert the object into a dict
stack_auto_update_version_policy_dict = stack_auto_update_version_policy_instance.to_dict()
# create an instance of StackAutoUpdateVersionPolicy from a dict
stack_auto_update_version_policy_from_dict = StackAutoUpdateVersionPolicy.from_dict(stack_auto_update_version_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


