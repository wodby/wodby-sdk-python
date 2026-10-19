# CloudGPU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manufacturer** | **str** |  | 
**model** | **str** |  | 
**count** | **int** |  | 
**memory_mi_b** | **int** | Memory per device in MiB; absent when the provider does not report it. | [optional] 

## Example

```python
from wodby.models.cloud_gpu import CloudGPU

# TODO update the JSON string below
json = "{}"
# create an instance of CloudGPU from a JSON string
cloud_gpu_instance = CloudGPU.from_json(json)
# print the JSON string representation of the object
print(CloudGPU.to_json())

# convert the object into a dict
cloud_gpu_dict = cloud_gpu_instance.to_dict()
# create an instance of CloudGPU from a dict
cloud_gpu_from_dict = CloudGPU.from_dict(cloud_gpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


