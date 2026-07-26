# StorageClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**provisioner** | **str** |  | 
**reclaim_policy** | **str** |  | [optional] 
**allow_volume_expansion** | **bool** |  | 
**mount_options** | **List[str]** |  | 
**volume_binding_mode** | **str** |  | [optional] 
**is_default** | **bool** |  | 
**selectable** | **bool** |  | 

## Example

```python
from wodby.models.storage_class import StorageClass

# TODO update the JSON string below
json = "{}"
# create an instance of StorageClass from a JSON string
storage_class_instance = StorageClass.from_json(json)
# print the JSON string representation of the object
print(StorageClass.to_json())

# convert the object into a dict
storage_class_dict = storage_class_instance.to_dict()
# create an instance of StorageClass from a dict
storage_class_from_dict = StorageClass.from_dict(storage_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


