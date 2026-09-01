# ProviderRevision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**icon** | **str** |  | 
**title** | **str** |  | 
**number** | **int** |  | 
**version** | **str** |  | 
**provider_id** | **int** |  | 
**manifest** | **Dict[str, object]** |  | [optional] 
**permission_audit** | **bool** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from wodby.models.provider_revision import ProviderRevision

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderRevision from a JSON string
provider_revision_instance = ProviderRevision.from_json(json)
# print the JSON string representation of the object
print(ProviderRevision.to_json())

# convert the object into a dict
provider_revision_dict = provider_revision_instance.to_dict()
# create an instance of ProviderRevision from a dict
provider_revision_from_dict = ProviderRevision.from_dict(provider_revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


