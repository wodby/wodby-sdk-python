# ClusterEnvironmentPolicyInput

Use envType and allowedEnvTypes. Legacy ID fields remain accepted but cannot be mixed with their type equivalents.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env_id** | **int** |  | [optional] 
**env_type** | **str** |  | [optional] 
**scope** | **str** |  | 
**allowed_env_ids** | **List[int]** |  | [optional] 
**allowed_env_types** | **List[str]** |  | [optional] 

## Example

```python
from wodby.models.cluster_environment_policy_input import ClusterEnvironmentPolicyInput

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterEnvironmentPolicyInput from a JSON string
cluster_environment_policy_input_instance = ClusterEnvironmentPolicyInput.from_json(json)
# print the JSON string representation of the object
print(ClusterEnvironmentPolicyInput.to_json())

# convert the object into a dict
cluster_environment_policy_input_dict = cluster_environment_policy_input_instance.to_dict()
# create an instance of ClusterEnvironmentPolicyInput from a dict
cluster_environment_policy_input_from_dict = ClusterEnvironmentPolicyInput.from_dict(cluster_environment_policy_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


