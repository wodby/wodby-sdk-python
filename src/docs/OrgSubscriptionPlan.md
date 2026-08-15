# OrgSubscriptionPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | 
**usage** | **float** |  | 
**usage_included** | **float** |  | 
**spending_limit** | **float** |  | 
**price_per_unit** | **float** |  | 

## Example

```python
from wodby.models.org_subscription_plan import OrgSubscriptionPlan

# TODO update the JSON string below
json = "{}"
# create an instance of OrgSubscriptionPlan from a JSON string
org_subscription_plan_instance = OrgSubscriptionPlan.from_json(json)
# print the JSON string representation of the object
print(OrgSubscriptionPlan.to_json())

# convert the object into a dict
org_subscription_plan_dict = org_subscription_plan_instance.to_dict()
# create an instance of OrgSubscriptionPlan from a dict
org_subscription_plan_from_dict = OrgSubscriptionPlan.from_dict(org_subscription_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


