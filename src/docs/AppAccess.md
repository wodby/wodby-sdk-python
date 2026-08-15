# AppAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**mode** | **str** |  | 
**scope** | **str** |  | 
**status** | **str** |  | 
**settings** | [**List[AppAccessSetting]**](AppAccessSetting.md) |  | 
**public_routes_suppressed** | **bool** |  | 
**effective_url** | **str** |  | [optional] 
**last_error** | **str** |  | [optional] 
**integration_id** | **int** |  | 
**endpoints** | [**List[AppAccessEndpoint]**](AppAccessEndpoint.md) |  | 
**resources** | [**List[AppAccessResource]**](AppAccessResource.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.app_access import AppAccess

# TODO update the JSON string below
json = "{}"
# create an instance of AppAccess from a JSON string
app_access_instance = AppAccess.from_json(json)
# print the JSON string representation of the object
print(AppAccess.to_json())

# convert the object into a dict
app_access_dict = app_access_instance.to_dict()
# create an instance of AppAccess from a dict
app_access_from_dict = AppAccess.from_dict(app_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


