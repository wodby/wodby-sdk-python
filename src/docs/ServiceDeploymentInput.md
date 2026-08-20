# ServiceDeploymentInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**image** | **str** |  | 
**unmanaged_image** | **bool** | Set by the CI build when the image was produced from a Dockerfile that does not derive from the service image. | [optional] 
**dockerfile_path** | **str** | Repository path of an author-provided Dockerfile, reported by the CI build. | [optional] 
**dockerfile_hash** | **str** | SHA-256 of the Dockerfile that produced the image, reported by the CI build. | [optional] 

## Example

```python
from wodby.models.service_deployment_input import ServiceDeploymentInput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeploymentInput from a JSON string
service_deployment_input_instance = ServiceDeploymentInput.from_json(json)
# print the JSON string representation of the object
print(ServiceDeploymentInput.to_json())

# convert the object into a dict
service_deployment_input_dict = service_deployment_input_instance.to_dict()
# create an instance of ServiceDeploymentInput from a dict
service_deployment_input_from_dict = ServiceDeploymentInput.from_dict(service_deployment_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


