# Cert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**custom** | **bool** |  | 
**issuer** | **str** | Human-readable certificate authority name parsed from uploaded certificates, or the managed issuer identifier. | 
**domain** | **str** |  | 
**dns_names** | **List[str]** |  | 
**route_ids** | **List[int]** |  | 
**fingerprint** | **str** |  | [optional] 
**key_type** | **str** |  | 
**key_length** | **int** |  | 
**status** | **str** |  | 
**app_instance_id** | **int** |  | [optional] 
**app_service_id** | **int** |  | [optional] 
**database_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**issued_at** | **datetime** |  | [optional] 
**renews_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 

## Example

```python
from wodby.models.cert import Cert

# TODO update the JSON string below
json = "{}"
# create an instance of Cert from a JSON string
cert_instance = Cert.from_json(json)
# print the JSON string representation of the object
print(Cert.to_json())

# convert the object into a dict
cert_dict = cert_instance.to_dict()
# create an instance of Cert from a dict
cert_from_dict = Cert.from_dict(cert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


