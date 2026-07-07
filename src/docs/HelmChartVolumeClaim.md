# HelmChartVolumeClaim


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**size** | **str** |  | [optional] 
**storage_class_name** | **str** |  | [optional] 
**access_modes** | **List[str]** |  | [optional] 

## Example

```python
from wodby.models.helm_chart_volume_claim import HelmChartVolumeClaim

# TODO update the JSON string below
json = "{}"
# create an instance of HelmChartVolumeClaim from a JSON string
helm_chart_volume_claim_instance = HelmChartVolumeClaim.from_json(json)
# print the JSON string representation of the object
print(HelmChartVolumeClaim.to_json())

# convert the object into a dict
helm_chart_volume_claim_dict = helm_chart_volume_claim_instance.to_dict()
# create an instance of HelmChartVolumeClaim from a dict
helm_chart_volume_claim_from_dict = HelmChartVolumeClaim.from_dict(helm_chart_volume_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


