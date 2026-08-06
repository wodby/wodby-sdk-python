# AppService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**type** | **str** |  | 
**status** | **str** |  | 
**replicas** | **int** |  | 
**scalability** | [**AppServiceScalability**](AppServiceScalability.md) |  | [optional] 
**version** | **str** |  | 
**main** | **bool** |  | 
**disabled** | **bool** |  | 
**external** | **bool** |  | 
**required** | **bool** |  | 
**needs_rebuild** | **bool** |  | 
**needs_redeploy** | **bool** |  | 
**configuration_ready** | **bool** |  | 
**app_instance_id** | **int** |  | 
**service_rev_id** | **int** |  | 
**parent_app_service_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.app_service import AppService

# TODO update the JSON string below
json = "{}"
# create an instance of AppService from a JSON string
app_service_instance = AppService.from_json(json)
# print the JSON string representation of the object
print(AppService.to_json())

# convert the object into a dict
app_service_dict = app_service_instance.to_dict()
# create an instance of AppService from a dict
app_service_from_dict = AppService.from_dict(app_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


