# ServiceRevisionChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | 
**icon** | **str** |  | 
**kind** | **str** |  | 
**previous_version** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**previous_rev_number** | **int** |  | [optional] 
**rev_number** | **int** |  | [optional] 
**entries** | [**List[StackServiceUpdateChangelogEntry]**](StackServiceUpdateChangelogEntry.md) |  | 

## Example

```python
from wodby.models.service_revision_change import ServiceRevisionChange

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceRevisionChange from a JSON string
service_revision_change_instance = ServiceRevisionChange.from_json(json)
# print the JSON string representation of the object
print(ServiceRevisionChange.to_json())

# convert the object into a dict
service_revision_change_dict = service_revision_change_instance.to_dict()
# create an instance of ServiceRevisionChange from a dict
service_revision_change_from_dict = ServiceRevisionChange.from_dict(service_revision_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


