# StackAutoOriginUpdateVersionPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | 
**allow_patch** | **bool** |  | 
**allow_minor** | **bool** |  | 
**allow_major** | **bool** |  | 

## Example

```python
from wodby.models.stack_auto_origin_update_version_policy import StackAutoOriginUpdateVersionPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of StackAutoOriginUpdateVersionPolicy from a JSON string
stack_auto_origin_update_version_policy_instance = StackAutoOriginUpdateVersionPolicy.from_json(json)
# print the JSON string representation of the object
print(StackAutoOriginUpdateVersionPolicy.to_json())

# convert the object into a dict
stack_auto_origin_update_version_policy_dict = stack_auto_origin_update_version_policy_instance.to_dict()
# create an instance of StackAutoOriginUpdateVersionPolicy from a dict
stack_auto_origin_update_version_policy_from_dict = StackAutoOriginUpdateVersionPolicy.from_dict(stack_auto_origin_update_version_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


