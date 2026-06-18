# CreateBuildRequest

App service IDs to build.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_service_ids** | **List[int]** |  | 

## Example

```python
from wodby.models.create_build_request import CreateBuildRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBuildRequest from a JSON string
create_build_request_instance = CreateBuildRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBuildRequest.to_json())

# convert the object into a dict
create_build_request_dict = create_build_request_instance.to_dict()
# create an instance of CreateBuildRequest from a dict
create_build_request_from_dict = CreateBuildRequest.from_dict(create_build_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


