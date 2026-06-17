# Env


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**type** | **str** |  | 
**org_id** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.env import Env

# TODO update the JSON string below
json = "{}"
# create an instance of Env from a JSON string
env_instance = Env.from_json(json)
# print the JSON string representation of the object
print(Env.to_json())

# convert the object into a dict
env_dict = env_instance.to_dict()
# create an instance of Env from a dict
env_from_dict = Env.from_dict(env_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


