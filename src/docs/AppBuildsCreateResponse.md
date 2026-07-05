# AppBuildsCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AppBuild]**](AppBuild.md) |  | 
**task_id** | **int** |  | [optional] 

## Example

```python
from wodby.models.app_builds_create_response import AppBuildsCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppBuildsCreateResponse from a JSON string
app_builds_create_response_instance = AppBuildsCreateResponse.from_json(json)
# print the JSON string representation of the object
print(AppBuildsCreateResponse.to_json())

# convert the object into a dict
app_builds_create_response_dict = app_builds_create_response_instance.to_dict()
# create an instance of AppBuildsCreateResponse from a dict
app_builds_create_response_from_dict = AppBuildsCreateResponse.from_dict(app_builds_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


