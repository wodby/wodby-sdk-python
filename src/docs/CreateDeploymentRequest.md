# CreateDeploymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**services** | [**List[AppServiceDeploymentRequest]**](AppServiceDeploymentRequest.md) |  | 
**skip_rollback** | **bool** |  | [optional] 

## Example

```python
from wodby.models.create_deployment_request import CreateDeploymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDeploymentRequest from a JSON string
create_deployment_request_instance = CreateDeploymentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDeploymentRequest.to_json())

# convert the object into a dict
create_deployment_request_dict = create_deployment_request_instance.to_dict()
# create an instance of CreateDeploymentRequest from a dict
create_deployment_request_from_dict = CreateDeploymentRequest.from_dict(create_deployment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


