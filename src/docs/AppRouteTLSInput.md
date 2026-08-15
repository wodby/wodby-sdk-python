# AppRouteTLSInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | 
**cert_id** | **int** | Required only when mode is CUSTOM. | [optional] 

## Example

```python
from wodby.models.app_route_tls_input import AppRouteTLSInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppRouteTLSInput from a JSON string
app_route_tls_input_instance = AppRouteTLSInput.from_json(json)
# print the JSON string representation of the object
print(AppRouteTLSInput.to_json())

# convert the object into a dict
app_route_tls_input_dict = app_route_tls_input_instance.to_dict()
# create an instance of AppRouteTLSInput from a dict
app_route_tls_input_from_dict = AppRouteTLSInput.from_dict(app_route_tls_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


