# ServiceWorkloadDeploymentConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**kind** | **str** |  | 
**override** | [**ServiceDeploymentPolicy**](ServiceDeploymentPolicy.md) |  | 
**effective** | [**ServiceDeploymentPolicy**](ServiceDeploymentPolicy.md) |  | 

## Example

```python
from wodby.models.service_workload_deployment_configuration import ServiceWorkloadDeploymentConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceWorkloadDeploymentConfiguration from a JSON string
service_workload_deployment_configuration_instance = ServiceWorkloadDeploymentConfiguration.from_json(json)
# print the JSON string representation of the object
print(ServiceWorkloadDeploymentConfiguration.to_json())

# convert the object into a dict
service_workload_deployment_configuration_dict = service_workload_deployment_configuration_instance.to_dict()
# create an instance of ServiceWorkloadDeploymentConfiguration from a dict
service_workload_deployment_configuration_from_dict = ServiceWorkloadDeploymentConfiguration.from_dict(service_workload_deployment_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


