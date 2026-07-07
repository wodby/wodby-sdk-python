# HelmChartMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**version** | **str** |  | [optional] 
**app_version** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**chart** | **str** |  | 

## Example

```python
from wodby.models.helm_chart_metadata import HelmChartMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of HelmChartMetadata from a JSON string
helm_chart_metadata_instance = HelmChartMetadata.from_json(json)
# print the JSON string representation of the object
print(HelmChartMetadata.to_json())

# convert the object into a dict
helm_chart_metadata_dict = helm_chart_metadata_instance.to_dict()
# create an instance of HelmChartMetadata from a dict
helm_chart_metadata_from_dict = HelmChartMetadata.from_dict(helm_chart_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


