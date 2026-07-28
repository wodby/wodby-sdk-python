# AppInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**status** | **str** |  | 
**main_domain** | **str** |  | [optional] 
**app_id** | **int** |  | 
**cluster_id** | **int** |  | 
**env_id** | **int** |  | 
**stack_id** | **int** |  | 
**stack_rev_id** | **int** |  | 
**stack_name** | **str** |  | 
**stack_title** | **str** |  | 
**stack_icon** | **str** |  | 
**stack_rev_number** | **int** |  | 
**stack_version** | **str** |  | 
**settings** | [**AppInstanceSettings**](AppInstanceSettings.md) |  | [optional] 
**health** | [**AppInstanceHealth**](AppInstanceHealth.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.app_instance import AppInstance

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstance from a JSON string
app_instance_instance = AppInstance.from_json(json)
# print the JSON string representation of the object
print(AppInstance.to_json())

# convert the object into a dict
app_instance_dict = app_instance_instance.to_dict()
# create an instance of AppInstance from a dict
app_instance_from_dict = AppInstance.from_dict(app_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


