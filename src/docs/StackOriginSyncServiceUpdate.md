# StackOriginSyncServiceUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stack_service_id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**service_title** | **str** |  | 
**previous_version** | **str** |  | 
**version** | **str** |  | 
**reason** | **str** | The origin&#39;s configuration that needs the newer version, such as option 3. | 
**refusal** | **str** | Why the sync can&#39;t update this stack service, such as a pin. Null when it can. | 

## Example

```python
from wodby.models.stack_origin_sync_service_update import StackOriginSyncServiceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of StackOriginSyncServiceUpdate from a JSON string
stack_origin_sync_service_update_instance = StackOriginSyncServiceUpdate.from_json(json)
# print the JSON string representation of the object
print(StackOriginSyncServiceUpdate.to_json())

# convert the object into a dict
stack_origin_sync_service_update_dict = stack_origin_sync_service_update_instance.to_dict()
# create an instance of StackOriginSyncServiceUpdate from a dict
stack_origin_sync_service_update_from_dict = StackOriginSyncServiceUpdate.from_dict(stack_origin_sync_service_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


