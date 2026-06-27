# AppServiceToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**app_service_id** | **int** |  | 
**name** | **str** |  | 
**value** | **str** |  | 
**value_secret_id** | **int** |  | [optional] 
**env_type** | **str** |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from wodby.models.app_service_token import AppServiceToken

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceToken from a JSON string
app_service_token_instance = AppServiceToken.from_json(json)
# print the JSON string representation of the object
print(AppServiceToken.to_json())

# convert the object into a dict
app_service_token_dict = app_service_token_instance.to_dict()
# create an instance of AppServiceToken from a dict
app_service_token_from_dict = AppServiceToken.from_dict(app_service_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


