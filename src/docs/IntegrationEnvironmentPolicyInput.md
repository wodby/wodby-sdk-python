# IntegrationEnvironmentPolicyInput

Use primaryEnvType and allowedEnvTypes. Legacy ID fields remain accepted but cannot be mixed with their type equivalents.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_env_id** | **int** |  | [optional] 
**primary_env_type** | **str** |  | [optional] 
**scope** | **str** |  | 
**allowed_env_ids** | **List[int]** |  | [optional] 
**allowed_env_types** | **List[str]** |  | [optional] 

## Example

```python
from wodby.models.integration_environment_policy_input import IntegrationEnvironmentPolicyInput

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationEnvironmentPolicyInput from a JSON string
integration_environment_policy_input_instance = IntegrationEnvironmentPolicyInput.from_json(json)
# print the JSON string representation of the object
print(IntegrationEnvironmentPolicyInput.to_json())

# convert the object into a dict
integration_environment_policy_input_dict = integration_environment_policy_input_instance.to_dict()
# create an instance of IntegrationEnvironmentPolicyInput from a dict
integration_environment_policy_input_from_dict = IntegrationEnvironmentPolicyInput.from_dict(integration_environment_policy_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


