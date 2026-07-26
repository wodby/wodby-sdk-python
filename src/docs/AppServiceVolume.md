# AppServiceVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**app_service_id** | **int** |  | 
**name** | **str** |  | 
**path** | **str** |  | 
**shared** | **bool** |  | 
**read_only** | **bool** |  | 
**size** | **int** |  | 
**configured_storage_class_name** | **str** |  | [optional] 
**effective_storage_class_names** | **List[str]** |  | 
**storage_class_status** | **str** |  | 
**storage_class_selectable** | **bool** |  | 
**from_volume_id** | **int** |  | [optional] 
**storage_app_service_id** | **int** |  | [optional] 

## Example

```python
from wodby.models.app_service_volume import AppServiceVolume

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceVolume from a JSON string
app_service_volume_instance = AppServiceVolume.from_json(json)
# print the JSON string representation of the object
print(AppServiceVolume.to_json())

# convert the object into a dict
app_service_volume_dict = app_service_volume_instance.to_dict()
# create an instance of AppServiceVolume from a dict
app_service_volume_from_dict = AppServiceVolume.from_dict(app_service_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


