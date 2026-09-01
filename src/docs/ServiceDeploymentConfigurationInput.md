# ServiceDeploymentConfigurationInput

Replaces the complete service-level deployment override. An empty object clears it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | [**ServiceDeploymentStrategy**](ServiceDeploymentStrategy.md) |  | [optional] 
**max_unavailable** | **str** | Absolute number or percentage, such as &#x60;0&#x60; or &#x60;25%&#x60;. | [optional] 
**max_surge** | **str** | Absolute number or percentage, such as &#x60;1&#x60; or &#x60;25%&#x60;. | [optional] 
**min_ready** | **str** | Go duration, such as &#x60;10s&#x60;. | [optional] 
**progress_deadline** | **str** | Go duration, such as &#x60;15m&#x60;. | [optional] 
**shutdown_grace_period** | **str** | Go duration, such as &#x60;11m&#x60;. | [optional] 
**workloads** | [**List[ServiceWorkloadDeploymentInput]**](ServiceWorkloadDeploymentInput.md) |  | [optional] 

## Example

```python
from wodby.models.service_deployment_configuration_input import ServiceDeploymentConfigurationInput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeploymentConfigurationInput from a JSON string
service_deployment_configuration_input_instance = ServiceDeploymentConfigurationInput.from_json(json)
# print the JSON string representation of the object
print(ServiceDeploymentConfigurationInput.to_json())

# convert the object into a dict
service_deployment_configuration_input_dict = service_deployment_configuration_input_instance.to_dict()
# create an instance of ServiceDeploymentConfigurationInput from a dict
service_deployment_configuration_input_from_dict = ServiceDeploymentConfigurationInput.from_dict(service_deployment_configuration_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


