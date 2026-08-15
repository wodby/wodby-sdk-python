# AppAccessEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**app_port_id** | **int** |  | 
**host** | **str** |  | 
**primary** | **bool** |  | 
**url** | **str** |  | 

## Example

```python
from wodby.models.app_access_endpoint import AppAccessEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of AppAccessEndpoint from a JSON string
app_access_endpoint_instance = AppAccessEndpoint.from_json(json)
# print the JSON string representation of the object
print(AppAccessEndpoint.to_json())

# convert the object into a dict
app_access_endpoint_dict = app_access_endpoint_instance.to_dict()
# create an instance of AppAccessEndpoint from a dict
app_access_endpoint_from_dict = AppAccessEndpoint.from_dict(app_access_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


