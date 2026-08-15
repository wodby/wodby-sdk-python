# AppServiceVolumeStorageClassState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume_id** | **int** |  | 
**configured_storage_class_name** | **str** |  | [optional] 
**effective_storage_class_names** | **List[str]** |  | 
**status** | **str** |  | 

## Example

```python
from wodby.models.app_service_volume_storage_class_state import AppServiceVolumeStorageClassState

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceVolumeStorageClassState from a JSON string
app_service_volume_storage_class_state_instance = AppServiceVolumeStorageClassState.from_json(json)
# print the JSON string representation of the object
print(AppServiceVolumeStorageClassState.to_json())

# convert the object into a dict
app_service_volume_storage_class_state_dict = app_service_volume_storage_class_state_instance.to_dict()
# create an instance of AppServiceVolumeStorageClassState from a dict
app_service_volume_storage_class_state_from_dict = AppServiceVolumeStorageClassState.from_dict(app_service_volume_storage_class_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


