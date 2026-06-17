# VolumeSizeInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**size** | **int** |  | 

## Example

```python
from wodby.models.volume_size_input import VolumeSizeInput

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeSizeInput from a JSON string
volume_size_input_instance = VolumeSizeInput.from_json(json)
# print the JSON string representation of the object
print(VolumeSizeInput.to_json())

# convert the object into a dict
volume_size_input_dict = volume_size_input_instance.to_dict()
# create an instance of VolumeSizeInput from a dict
volume_size_input_from_dict = VolumeSizeInput.from_dict(volume_size_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


