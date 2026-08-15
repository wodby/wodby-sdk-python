# AddAppServiceVolumeInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**size** | **int** |  | [optional] 
**storage_class_name** | **str** |  | [optional] 

## Example

```python
from wodby.models.add_app_service_volume_input import AddAppServiceVolumeInput

# TODO update the JSON string below
json = "{}"
# create an instance of AddAppServiceVolumeInput from a JSON string
add_app_service_volume_input_instance = AddAppServiceVolumeInput.from_json(json)
# print the JSON string representation of the object
print(AddAppServiceVolumeInput.to_json())

# convert the object into a dict
add_app_service_volume_input_dict = add_app_service_volume_input_instance.to_dict()
# create an instance of AddAppServiceVolumeInput from a dict
add_app_service_volume_input_from_dict = AddAppServiceVolumeInput.from_dict(add_app_service_volume_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


