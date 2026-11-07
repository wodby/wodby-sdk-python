# OrgUsagePeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** |  | 
**end** | **datetime** | Where the period ends. A past period ends where the next one starts; a plan change starts a new period early. | 
**current** | **bool** | The subscription&#39;s current period, whose usage is still growing. | 

## Example

```python
from wodby.models.org_usage_period import OrgUsagePeriod

# TODO update the JSON string below
json = "{}"
# create an instance of OrgUsagePeriod from a JSON string
org_usage_period_instance = OrgUsagePeriod.from_json(json)
# print the JSON string representation of the object
print(OrgUsagePeriod.to_json())

# convert the object into a dict
org_usage_period_dict = org_usage_period_instance.to_dict()
# create an instance of OrgUsagePeriod from a dict
org_usage_period_from_dict = OrgUsagePeriod.from_dict(org_usage_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


