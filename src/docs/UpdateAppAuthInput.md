# UpdateAppAuthInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_service_ids** | **List[int]** | App services to protect. Omit every scope field to preserve the current scope, or pass an empty list to protect the whole app environment. | [optional] 
**app_service_id** | **int** | Single-service scope. Ignored when appServiceIds is supplied. | [optional] 
**app_route_id** | **int** | Moves the entry to route scope. The owning app service is derived from the route. | [optional] 
**login** | **str** |  | 
**password** | **str** | Replaces the existing secret when supplied; omit to keep the current password. | [optional] 
**realm** | **str** |  | 

## Example

```python
from wodby.models.update_app_auth_input import UpdateAppAuthInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAppAuthInput from a JSON string
update_app_auth_input_instance = UpdateAppAuthInput.from_json(json)
# print the JSON string representation of the object
print(UpdateAppAuthInput.to_json())

# convert the object into a dict
update_app_auth_input_dict = update_app_auth_input_instance.to_dict()
# create an instance of UpdateAppAuthInput from a dict
update_app_auth_input_from_dict = UpdateAppAuthInput.from_dict(update_app_auth_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


