# StackServiceSecurityFix

A vulnerability that updating a stack service to its service's latest version fixes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vulnerability_id** | **str** | The CVE ID when there is one, otherwise the advisory&#39;s own ID. | 
**severity** | **str** |  | 
**package_name** | **str** |  | 
**package_version** | **str** | The vulnerable version in the image the stack service deploys now. | 
**exploited** | **bool** | Whether the vulnerability is on CISA&#39;s catalog of known exploited vulnerabilities. | 
**epss** | **float** | The EPSS probability that the vulnerability is exploited in the next 30 days, from 0 to 1. Absent when unknown. | [optional] 
**tracked** | **bool** | Whether Wodby tracks the vulnerability itself because public databases don&#39;t list it yet. | 
**url** | **str** | The vulnerability&#39;s public record. Absent when there is none. | [optional] 
**option_versions** | **List[str]** | The stack service&#39;s option versions whose images have the vulnerability, such as 8.3 and 8.4. | 

## Example

```python
from wodby.models.stack_service_security_fix import StackServiceSecurityFix

# TODO update the JSON string below
json = "{}"
# create an instance of StackServiceSecurityFix from a JSON string
stack_service_security_fix_instance = StackServiceSecurityFix.from_json(json)
# print the JSON string representation of the object
print(StackServiceSecurityFix.to_json())

# convert the object into a dict
stack_service_security_fix_dict = stack_service_security_fix_instance.to_dict()
# create an instance of StackServiceSecurityFix from a dict
stack_service_security_fix_from_dict = StackServiceSecurityFix.from_dict(stack_service_security_fix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


