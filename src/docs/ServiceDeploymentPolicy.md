# ServiceDeploymentPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | [**ServiceDeploymentStrategy**](ServiceDeploymentStrategy.md) |  | [optional] 
**max_unavailable** | **str** | Absolute number or percentage, such as &#x60;0&#x60; or &#x60;25%&#x60;. | [optional] 
**max_surge** | **str** | Absolute number or percentage, such as &#x60;1&#x60; or &#x60;25%&#x60;. | [optional] 
**min_ready** | **str** | Go duration, such as &#x60;10s&#x60;. | [optional] 
**progress_deadline** | **str** | Go duration, such as &#x60;15m&#x60;. | [optional] 
**shutdown_grace_period** | **str** | Go duration, such as &#x60;11m&#x60;. | [optional] 

## Example

```python
from wodby.models.service_deployment_policy import ServiceDeploymentPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeploymentPolicy from a JSON string
service_deployment_policy_instance = ServiceDeploymentPolicy.from_json(json)
# print the JSON string representation of the object
print(ServiceDeploymentPolicy.to_json())

# convert the object into a dict
service_deployment_policy_dict = service_deployment_policy_instance.to_dict()
# create an instance of ServiceDeploymentPolicy from a dict
service_deployment_policy_from_dict = ServiceDeploymentPolicy.from_dict(service_deployment_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


