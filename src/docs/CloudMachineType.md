# CloudMachineType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**cpu** | **int** |  | [optional] 
**mem** | **int** |  | [optional] 
**disk** | **int** |  | [optional] 
**shared_cpu** | **bool** |  | [optional] 
**available** | **bool** |  | [optional] 
**family** | **str** |  | [optional] 
**min_storage_size** | **int** |  | [optional] 
**max_storage_size** | **int** |  | [optional] 
**min_iops** | **int** |  | [optional] 
**max_iops** | **int** |  | [optional] 
**default_iops** | **int** |  | [optional] 
**storage_options** | **List[Dict[str, object]]** |  | [optional] 
**gpus** | [**List[CloudGPU]**](CloudGPU.md) | Provider-reported devices. This does not guarantee driver setup or spare capacity. | [optional] 

## Example

```python
from wodby.models.cloud_machine_type import CloudMachineType

# TODO update the JSON string below
json = "{}"
# create an instance of CloudMachineType from a JSON string
cloud_machine_type_instance = CloudMachineType.from_json(json)
# print the JSON string representation of the object
print(CloudMachineType.to_json())

# convert the object into a dict
cloud_machine_type_dict = cloud_machine_type_instance.to_dict()
# create an instance of CloudMachineType from a dict
cloud_machine_type_from_dict = CloudMachineType.from_dict(cloud_machine_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


