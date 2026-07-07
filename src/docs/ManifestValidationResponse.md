# ManifestValidationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** |  | 
**error** | **str** |  | [optional] 
**resource** | **Dict[str, object]** |  | [optional] 
**manifest** | **Dict[str, object]** |  | [optional] 

## Example

```python
from wodby.models.manifest_validation_response import ManifestValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ManifestValidationResponse from a JSON string
manifest_validation_response_instance = ManifestValidationResponse.from_json(json)
# print the JSON string representation of the object
print(ManifestValidationResponse.to_json())

# convert the object into a dict
manifest_validation_response_dict = manifest_validation_response_instance.to_dict()
# create an instance of ManifestValidationResponse from a dict
manifest_validation_response_from_dict = ManifestValidationResponse.from_dict(manifest_validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


