# AppServiceBuild


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**status** | **str** |  | 
**image** | **str** |  | 
**image_deleted** | **bool** |  | 
**unmanaged_image** | **bool** | True when the image was built from a Dockerfile that does not derive from the service image, so it no longer tracks service image updates. | 
**dockerfile_path** | **str** | Repository path of an author-provided Dockerfile. Empty when the build used a service-provided or generated Dockerfile. | 
**dockerfile_hash** | **str** | SHA-256 of the Dockerfile that produced the image. Empty when the build did not report it. | 
**size** | **int** |  | 
**app_service_id** | **int** |  | 
**previously_deployed** | **bool** |  | 
**currently_deployed** | **bool** |  | 
**current_build_number** | **int** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.app_service_build import AppServiceBuild

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceBuild from a JSON string
app_service_build_instance = AppServiceBuild.from_json(json)
# print the JSON string representation of the object
print(AppServiceBuild.to_json())

# convert the object into a dict
app_service_build_dict = app_service_build_instance.to_dict()
# create an instance of AppServiceBuild from a dict
app_service_build_from_dict = AppServiceBuild.from_dict(app_service_build_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


