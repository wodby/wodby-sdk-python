# AppBuildsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AppBuild]**](AppBuild.md) |  | 
**total_count** | **int** |  | 
**next_page** | **int** |  | [optional] 

## Example

```python
from wodby.models.app_builds_response import AppBuildsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppBuildsResponse from a JSON string
app_builds_response_instance = AppBuildsResponse.from_json(json)
# print the JSON string representation of the object
print(AppBuildsResponse.to_json())

# convert the object into a dict
app_builds_response_dict = app_builds_response_instance.to_dict()
# create an instance of AppBuildsResponse from a dict
app_builds_response_from_dict = AppBuildsResponse.from_dict(app_builds_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


