# AppDeploymentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AppDeployment]**](AppDeployment.md) |  | 
**total_count** | **int** |  | 
**next_page** | **int** |  | [optional] 

## Example

```python
from wodby.models.app_deployments_response import AppDeploymentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppDeploymentsResponse from a JSON string
app_deployments_response_instance = AppDeploymentsResponse.from_json(json)
# print the JSON string representation of the object
print(AppDeploymentsResponse.to_json())

# convert the object into a dict
app_deployments_response_dict = app_deployments_response_instance.to_dict()
# create an instance of AppDeploymentsResponse from a dict
app_deployments_response_from_dict = AppDeploymentsResponse.from_dict(app_deployments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


