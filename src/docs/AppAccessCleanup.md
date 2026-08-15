# AppAccessCleanup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**app_access_id** | **int** |  | 
**app_instance_id** | **int** |  | 
**integration_id** | **int** |  | 
**provider** | **str** |  | 
**status** | **str** |  | 
**attempts** | **int** |  | 
**last_error** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.app_access_cleanup import AppAccessCleanup

# TODO update the JSON string below
json = "{}"
# create an instance of AppAccessCleanup from a JSON string
app_access_cleanup_instance = AppAccessCleanup.from_json(json)
# print the JSON string representation of the object
print(AppAccessCleanup.to_json())

# convert the object into a dict
app_access_cleanup_dict = app_access_cleanup_instance.to_dict()
# create an instance of AppAccessCleanup from a dict
app_access_cleanup_from_dict = AppAccessCleanup.from_dict(app_access_cleanup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


