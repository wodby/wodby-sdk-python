# AppServiceHelmValueSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_service** | **bool** |  | 
**from_stack** | **bool** |  | 

## Example

```python
from wodby.models.app_service_helm_value_source import AppServiceHelmValueSource

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceHelmValueSource from a JSON string
app_service_helm_value_source_instance = AppServiceHelmValueSource.from_json(json)
# print the JSON string representation of the object
print(AppServiceHelmValueSource.to_json())

# convert the object into a dict
app_service_helm_value_source_dict = app_service_helm_value_source_instance.to_dict()
# create an instance of AppServiceHelmValueSource from a dict
app_service_helm_value_source_from_dict = AppServiceHelmValueSource.from_dict(app_service_helm_value_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


