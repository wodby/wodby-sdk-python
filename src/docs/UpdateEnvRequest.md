# UpdateEnvRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from wodby.models.update_env_request import UpdateEnvRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEnvRequest from a JSON string
update_env_request_instance = UpdateEnvRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateEnvRequest.to_json())

# convert the object into a dict
update_env_request_dict = update_env_request_instance.to_dict()
# create an instance of UpdateEnvRequest from a dict
update_env_request_from_dict = UpdateEnvRequest.from_dict(update_env_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


