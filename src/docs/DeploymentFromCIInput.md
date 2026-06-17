# DeploymentFromCIInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_build_id** | **int** |  | 
**services** | [**List[ServiceDeploymentInput]**](ServiceDeploymentInput.md) |  | 
**skip_post_deployment** | **bool** |  | 

## Example

```python
from wodby.models.deployment_from_ci_input import DeploymentFromCIInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentFromCIInput from a JSON string
deployment_from_ci_input_instance = DeploymentFromCIInput.from_json(json)
# print the JSON string representation of the object
print(DeploymentFromCIInput.to_json())

# convert the object into a dict
deployment_from_ci_input_dict = deployment_from_ci_input_instance.to_dict()
# create an instance of DeploymentFromCIInput from a dict
deployment_from_ci_input_from_dict = DeploymentFromCIInput.from_dict(deployment_from_ci_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


