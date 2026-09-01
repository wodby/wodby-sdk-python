# ServiceWorkloadDeploymentInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | [**ServiceDeploymentStrategy**](ServiceDeploymentStrategy.md) |  | [optional] 
**max_unavailable** | **str** | Absolute number or percentage, such as &#x60;0&#x60; or &#x60;25%&#x60;. | [optional] 
**max_surge** | **str** | Absolute number or percentage, such as &#x60;1&#x60; or &#x60;25%&#x60;. | [optional] 
**min_ready** | **str** | Go duration, such as &#x60;10s&#x60;. | [optional] 
**progress_deadline** | **str** | Go duration, such as &#x60;15m&#x60;. | [optional] 
**shutdown_grace_period** | **str** | Go duration, such as &#x60;11m&#x60;. | [optional] 
**name** | **str** |  | 

## Example

```python
from wodby.models.service_workload_deployment_input import ServiceWorkloadDeploymentInput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceWorkloadDeploymentInput from a JSON string
service_workload_deployment_input_instance = ServiceWorkloadDeploymentInput.from_json(json)
# print the JSON string representation of the object
print(ServiceWorkloadDeploymentInput.to_json())

# convert the object into a dict
service_workload_deployment_input_dict = service_workload_deployment_input_instance.to_dict()
# create an instance of ServiceWorkloadDeploymentInput from a dict
service_workload_deployment_input_from_dict = ServiceWorkloadDeploymentInput.from_dict(service_workload_deployment_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


