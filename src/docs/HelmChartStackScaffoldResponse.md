# HelmChartStackScaffoldResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | [**HelmChartAnalysis**](HelmChartAnalysis.md) |  | 
**service_manifest_yaml** | **str** |  | 
**service_manifest** | **Dict[str, object]** |  | 
**stack_manifest_yaml** | **str** |  | 
**stack_manifest** | **Dict[str, object]** |  | 
**warnings** | **List[str]** |  | [optional] 

## Example

```python
from wodby.models.helm_chart_stack_scaffold_response import HelmChartStackScaffoldResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HelmChartStackScaffoldResponse from a JSON string
helm_chart_stack_scaffold_response_instance = HelmChartStackScaffoldResponse.from_json(json)
# print the JSON string representation of the object
print(HelmChartStackScaffoldResponse.to_json())

# convert the object into a dict
helm_chart_stack_scaffold_response_dict = helm_chart_stack_scaffold_response_instance.to_dict()
# create an instance of HelmChartStackScaffoldResponse from a dict
helm_chart_stack_scaffold_response_from_dict = HelmChartStackScaffoldResponse.from_dict(helm_chart_stack_scaffold_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


