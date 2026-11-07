# OrgUsageReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | [**OrgUsagePeriod**](OrgUsagePeriod.md) |  | 
**amount** | **float** | Total of all projects at the public list price in USD. | 
**invoice_amount** | **float** | What the invoices charged for the report&#39;s items in the period, in USD before tax. Null while it is unknown: for the current period, a period that was not invoiced, or while an invoice is a draft. | 
**projects** | [**List[OrgUsageProject]**](OrgUsageProject.md) | Projects ordered by title, with the organization row last. | 

## Example

```python
from wodby.models.org_usage_report import OrgUsageReport

# TODO update the JSON string below
json = "{}"
# create an instance of OrgUsageReport from a JSON string
org_usage_report_instance = OrgUsageReport.from_json(json)
# print the JSON string representation of the object
print(OrgUsageReport.to_json())

# convert the object into a dict
org_usage_report_dict = org_usage_report_instance.to_dict()
# create an instance of OrgUsageReport from a dict
org_usage_report_from_dict = OrgUsageReport.from_dict(org_usage_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


