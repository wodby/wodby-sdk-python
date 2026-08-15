# Org


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**domain** | **str** |  | 
**default_time_zone** | **str** |  | 
**ci_integration_id** | **int** | Effective default CI integration ID. Zero selects the built-in Wodby CI service. | 
**registry_integration_id** | **int** | Effective default registry integration ID. Zero selects the built-in Wodby registry service. | 
**capabilities** | [**OrgCapabilities**](OrgCapabilities.md) |  | [optional] 
**subscription** | [**OrgSubscription**](OrgSubscription.md) |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.org import Org

# TODO update the JSON string below
json = "{}"
# create an instance of Org from a JSON string
org_instance = Org.from_json(json)
# print the JSON string representation of the object
print(Org.to_json())

# convert the object into a dict
org_dict = org_instance.to_dict()
# create an instance of Org from a dict
org_from_dict = Org.from_dict(org_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


