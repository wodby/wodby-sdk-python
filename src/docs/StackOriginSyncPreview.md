# StackOriginSyncPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous_version** | **str** |  | 
**version** | **str** |  | 
**service_updates** | [**List[StackOriginSyncServiceUpdate]**](StackOriginSyncServiceUpdate.md) | Stack services the sync has to update to the service version the origin uses. The sync needs updateStackServices to update them. | 
**error** | **str** | Why the sync would fail. Null when it would go through once the listed stack services may be updated. | 
**changes** | [**List[LogLine]**](LogLine.md) | What the sync would change, as its task log will list it. Empty when it would fail. | 

## Example

```python
from wodby.models.stack_origin_sync_preview import StackOriginSyncPreview

# TODO update the JSON string below
json = "{}"
# create an instance of StackOriginSyncPreview from a JSON string
stack_origin_sync_preview_instance = StackOriginSyncPreview.from_json(json)
# print the JSON string representation of the object
print(StackOriginSyncPreview.to_json())

# convert the object into a dict
stack_origin_sync_preview_dict = stack_origin_sync_preview_instance.to_dict()
# create an instance of StackOriginSyncPreview from a dict
stack_origin_sync_preview_from_dict = StackOriginSyncPreview.from_dict(stack_origin_sync_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


