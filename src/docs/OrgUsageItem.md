# OrgUsageItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | **str** |  | 
**title** | **str** |  | 
**quantity** | **float** | Usage in unit over the period. | 
**unit** | **str** | service-hour, minute, GB-hour, or USD for Wodby Cloud usage. | 
**amount** | **float** | Quantity at the public list price in USD, before included usage and discounts. | 
**invoice_share** | **float** | This entry&#39;s share of what the invoices charged for the item&#39;s usage in the period, in USD before tax: the invoiced amount after included usage, discounts, and prorations, split between projects in proportion to amount. An item invoiced without recorded usage is shared to the organization row. Null while the invoiced amount is unknown. | 

## Example

```python
from wodby.models.org_usage_item import OrgUsageItem

# TODO update the JSON string below
json = "{}"
# create an instance of OrgUsageItem from a JSON string
org_usage_item_instance = OrgUsageItem.from_json(json)
# print the JSON string representation of the object
print(OrgUsageItem.to_json())

# convert the object into a dict
org_usage_item_dict = org_usage_item_instance.to_dict()
# create an instance of OrgUsageItem from a dict
org_usage_item_from_dict = OrgUsageItem.from_dict(org_usage_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


