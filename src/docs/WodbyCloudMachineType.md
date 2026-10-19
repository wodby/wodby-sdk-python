# WodbyCloudMachineType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | 
**shared_cpu** | **bool** |  | 
**price_hourly** | **float** |  | 
**price_monthly** | **float** |  | 
**disk** | **int** | Node disk size in GB. | 

## Example

```python
from wodby.models.wodby_cloud_machine_type import WodbyCloudMachineType

# TODO update the JSON string below
json = "{}"
# create an instance of WodbyCloudMachineType from a JSON string
wodby_cloud_machine_type_instance = WodbyCloudMachineType.from_json(json)
# print the JSON string representation of the object
print(WodbyCloudMachineType.to_json())

# convert the object into a dict
wodby_cloud_machine_type_dict = wodby_cloud_machine_type_instance.to_dict()
# create an instance of WodbyCloudMachineType from a dict
wodby_cloud_machine_type_from_dict = WodbyCloudMachineType.from_dict(wodby_cloud_machine_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


