# OrgSubscriptionPlanDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | 
**usage** | **float** |  | 
**usage_included** | **float** |  | 
**spending_limit** | **float** |  | 
**price_per_unit** | **float** |  | 
**unit** | **str** |  | 

## Example

```python
from wodby.models.org_subscription_plan_details import OrgSubscriptionPlanDetails

# TODO update the JSON string below
json = "{}"
# create an instance of OrgSubscriptionPlanDetails from a JSON string
org_subscription_plan_details_instance = OrgSubscriptionPlanDetails.from_json(json)
# print the JSON string representation of the object
print(OrgSubscriptionPlanDetails.to_json())

# convert the object into a dict
org_subscription_plan_details_dict = org_subscription_plan_details_instance.to_dict()
# create an instance of OrgSubscriptionPlanDetails from a dict
org_subscription_plan_details_from_dict = OrgSubscriptionPlanDetails.from_dict(org_subscription_plan_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


