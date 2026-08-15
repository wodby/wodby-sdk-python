# AppAccessResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**type** | **str** |  | 
**name** | **str** |  | 
**external_id** | **str** |  | 
**status** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.app_access_resource import AppAccessResource

# TODO update the JSON string below
json = "{}"
# create an instance of AppAccessResource from a JSON string
app_access_resource_instance = AppAccessResource.from_json(json)
# print the JSON string representation of the object
print(AppAccessResource.to_json())

# convert the object into a dict
app_access_resource_dict = app_access_resource_instance.to_dict()
# create an instance of AppAccessResource from a dict
app_access_resource_from_dict = AppAccessResource.from_dict(app_access_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


