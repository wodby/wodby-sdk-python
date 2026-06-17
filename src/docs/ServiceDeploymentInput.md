# ServiceDeploymentInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**image** | **str** |  | 

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


