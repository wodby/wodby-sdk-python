# StackServiceUpdateChangelog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stack_service_id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**previous_version** | **str** |  | 
**version** | **str** |  | 
**previous_rev_number** | **int** |  | 
**rev_number** | **int** |  | 
**entries** | [**List[StackServiceUpdateChangelogEntry]**](StackServiceUpdateChangelogEntry.md) |  | 

## Example

```python
from wodby.models.stack_service_update_changelog import StackServiceUpdateChangelog

# TODO update the JSON string below
json = "{}"
# create an instance of StackServiceUpdateChangelog from a JSON string
stack_service_update_changelog_instance = StackServiceUpdateChangelog.from_json(json)
# print the JSON string representation of the object
print(StackServiceUpdateChangelog.to_json())

# convert the object into a dict
stack_service_update_changelog_dict = stack_service_update_changelog_instance.to_dict()
# create an instance of StackServiceUpdateChangelog from a dict
stack_service_update_changelog_from_dict = StackServiceUpdateChangelog.from_dict(stack_service_update_changelog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


