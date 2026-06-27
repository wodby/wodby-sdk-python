# AppPort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**protocol** | **str** |  | 
**number** | **int** |  | 
**public_port** | **int** |  | [optional] 
**private** | **bool** |  | 
**app_endpoint_id** | **int** |  | 
**app_instance_id** | **int** |  | 
**app_service_id** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.app_port import AppPort

# TODO update the JSON string below
json = "{}"
# create an instance of AppPort from a JSON string
app_port_instance = AppPort.from_json(json)
# print the JSON string representation of the object
print(AppPort.to_json())

# convert the object into a dict
app_port_dict = app_port_instance.to_dict()
# create an instance of AppPort from a dict
app_port_from_dict = AppPort.from_dict(app_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


