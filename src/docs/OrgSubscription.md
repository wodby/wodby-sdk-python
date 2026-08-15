# OrgSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**plan** | [**OrgSubscriptionPlan**](OrgSubscriptionPlan.md) |  | [optional] 

## Example

```python
from wodby.models.org_subscription import OrgSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of OrgSubscription from a JSON string
org_subscription_instance = OrgSubscription.from_json(json)
# print the JSON string representation of the object
print(OrgSubscription.to_json())

# convert the object into a dict
org_subscription_dict = org_subscription_instance.to_dict()
# create an instance of OrgSubscription from a dict
org_subscription_from_dict = OrgSubscription.from_dict(org_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


