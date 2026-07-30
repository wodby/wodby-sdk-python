# ServiceRevision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**type** | **str** |  | 
**external** | **bool** |  | 
**number** | **int** |  | 
**version** | **str** |  | 
**service_id** | **int** |  | 
**manifest** | [**ServiceManifest**](ServiceManifest.md) |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from wodby.models.service_revision import ServiceRevision

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceRevision from a JSON string
service_revision_instance = ServiceRevision.from_json(json)
# print the JSON string representation of the object
print(ServiceRevision.to_json())

# convert the object into a dict
service_revision_dict = service_revision_instance.to_dict()
# create an instance of ServiceRevision from a dict
service_revision_from_dict = ServiceRevision.from_dict(service_revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


