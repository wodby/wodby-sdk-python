# StackOriginSyncChangelog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous_version** | **str** |  | 
**version** | **str** |  | 
**entries** | [**List[StackServiceUpdateChangelogEntry]**](StackServiceUpdateChangelogEntry.md) |  | 

## Example

```python
from wodby.models.stack_origin_sync_changelog import StackOriginSyncChangelog

# TODO update the JSON string below
json = "{}"
# create an instance of StackOriginSyncChangelog from a JSON string
stack_origin_sync_changelog_instance = StackOriginSyncChangelog.from_json(json)
# print the JSON string representation of the object
print(StackOriginSyncChangelog.to_json())

# convert the object into a dict
stack_origin_sync_changelog_dict = stack_origin_sync_changelog_instance.to_dict()
# create an instance of StackOriginSyncChangelog from a dict
stack_origin_sync_changelog_from_dict = StackOriginSyncChangelog.from_dict(stack_origin_sync_changelog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


