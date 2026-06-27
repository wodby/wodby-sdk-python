# NewAppInstanceInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **int** |  | 
**instance_name** | **str** |  | 
**instance_title** | **str** |  | 
**domain** | **str** |  | 
**stack_rev_id** | **int** |  | 
**services** | [**List[NewAppServiceInput]**](NewAppServiceInput.md) |  | 
**cluster_id** | **int** |  | [optional] 
**env_id** | **int** |  | 
**ci_integration_id** | **int** |  | [optional] 
**registry_integration_id** | **int** |  | [optional] 

## Example

```python
from wodby.models.new_app_instance_input import NewAppInstanceInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewAppInstanceInput from a JSON string
new_app_instance_input_instance = NewAppInstanceInput.from_json(json)
# print the JSON string representation of the object
print(NewAppInstanceInput.to_json())

# convert the object into a dict
new_app_instance_input_dict = new_app_instance_input_instance.to_dict()
# create an instance of NewAppInstanceInput from a dict
new_app_instance_input_from_dict = NewAppInstanceInput.from_dict(new_app_instance_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


