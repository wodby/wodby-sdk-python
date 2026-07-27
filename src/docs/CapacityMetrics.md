# CapacityMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**allocated** | **int** |  | 

## Example

```python
from wodby.models.capacity_metrics import CapacityMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityMetrics from a JSON string
capacity_metrics_instance = CapacityMetrics.from_json(json)
# print the JSON string representation of the object
print(CapacityMetrics.to_json())

# convert the object into a dict
capacity_metrics_dict = capacity_metrics_instance.to_dict()
# create an instance of CapacityMetrics from a dict
capacity_metrics_from_dict = CapacityMetrics.from_dict(capacity_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


