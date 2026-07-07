# ManifestFromYAMLInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** | Optional for API-key requests; defaults to the API key&#39;s organization. | [optional] 
**project_id** | **int** |  | [optional] 
**version** | **str** | Optional revision version label for the generated non-Git resource. | [optional] 
**manifest_yaml** | **str** | Complete Wodby service.yml or stack.yml manifest content. | 
**files** | **Dict[str, str]** | Optional referenced file contents keyed by manifest-relative path, for example Dockerfile or configs/app.conf. | [optional] 

## Example

```python
from wodby.models.manifest_from_yaml_input import ManifestFromYAMLInput

# TODO update the JSON string below
json = "{}"
# create an instance of ManifestFromYAMLInput from a JSON string
manifest_from_yaml_input_instance = ManifestFromYAMLInput.from_json(json)
# print the JSON string representation of the object
print(ManifestFromYAMLInput.to_json())

# convert the object into a dict
manifest_from_yaml_input_dict = manifest_from_yaml_input_instance.to_dict()
# create an instance of ManifestFromYAMLInput from a dict
manifest_from_yaml_input_from_dict = ManifestFromYAMLInput.from_dict(manifest_from_yaml_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


