# StackServiceUpdateChangelogEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from wodby.models.stack_service_update_changelog_entry import StackServiceUpdateChangelogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of StackServiceUpdateChangelogEntry from a JSON string
stack_service_update_changelog_entry_instance = StackServiceUpdateChangelogEntry.from_json(json)
# print the JSON string representation of the object
print(StackServiceUpdateChangelogEntry.to_json())

# convert the object into a dict
stack_service_update_changelog_entry_dict = stack_service_update_changelog_entry_instance.to_dict()
# create an instance of StackServiceUpdateChangelogEntry from a dict
stack_service_update_changelog_entry_from_dict = StackServiceUpdateChangelogEntry.from_dict(stack_service_update_changelog_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


