# GPUResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_name** | **str** | Qualified device-plugin resource name, such as nvidia.com/gpu or amd.com/gpu. Native and reserved Kubernetes resource names are rejected. | 
**count** | **int** | Device count per container replica. Kubernetes requests and limits are equal; zero explicitly disables GPUs. | 

## Example

```python
from wodby.models.gpu_resources import GPUResources

# TODO update the JSON string below
json = "{}"
# create an instance of GPUResources from a JSON string
gpu_resources_instance = GPUResources.from_json(json)
# print the JSON string representation of the object
print(GPUResources.to_json())

# convert the object into a dict
gpu_resources_dict = gpu_resources_instance.to_dict()
# create an instance of GPUResources from a dict
gpu_resources_from_dict = GPUResources.from_dict(gpu_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


