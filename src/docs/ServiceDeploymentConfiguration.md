# ServiceDeploymentConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**override** | [**ServiceDeploymentPolicy**](ServiceDeploymentPolicy.md) |  | 
**effective** | [**ServiceDeploymentPolicy**](ServiceDeploymentPolicy.md) |  | 
**workloads** | [**List[ServiceWorkloadDeploymentConfiguration]**](ServiceWorkloadDeploymentConfiguration.md) |  | 

## Example

```python
from wodby.models.service_deployment_configuration import ServiceDeploymentConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeploymentConfiguration from a JSON string
service_deployment_configuration_instance = ServiceDeploymentConfiguration.from_json(json)
# print the JSON string representation of the object
print(ServiceDeploymentConfiguration.to_json())

# convert the object into a dict
service_deployment_configuration_dict = service_deployment_configuration_instance.to_dict()
# create an instance of ServiceDeploymentConfiguration from a dict
service_deployment_configuration_from_dict = ServiceDeploymentConfiguration.from_dict(service_deployment_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


