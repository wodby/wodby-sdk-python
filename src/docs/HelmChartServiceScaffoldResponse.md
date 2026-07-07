# HelmChartServiceScaffoldResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | [**HelmChartAnalysis**](HelmChartAnalysis.md) |  | 
**manifest_yaml** | **str** |  | 
**manifest** | **Dict[str, object]** |  | 
**warnings** | **List[str]** |  | [optional] 

## Example

```python
from wodby.models.helm_chart_service_scaffold_response import HelmChartServiceScaffoldResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HelmChartServiceScaffoldResponse from a JSON string
helm_chart_service_scaffold_response_instance = HelmChartServiceScaffoldResponse.from_json(json)
# print the JSON string representation of the object
print(HelmChartServiceScaffoldResponse.to_json())

# convert the object into a dict
helm_chart_service_scaffold_response_dict = helm_chart_service_scaffold_response_instance.to_dict()
# create an instance of HelmChartServiceScaffoldResponse from a dict
helm_chart_service_scaffold_response_from_dict = HelmChartServiceScaffoldResponse.from_dict(helm_chart_service_scaffold_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


