# CreateEnvRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from wodby.models.create_env_request import CreateEnvRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEnvRequest from a JSON string
create_env_request_instance = CreateEnvRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEnvRequest.to_json())

# convert the object into a dict
create_env_request_dict = create_env_request_instance.to_dict()
# create an instance of CreateEnvRequest from a dict
create_env_request_from_dict = CreateEnvRequest.from_dict(create_env_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


