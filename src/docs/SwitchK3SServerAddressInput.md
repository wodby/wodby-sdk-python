# SwitchK3SServerAddressInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | A private address from GET /cluster-k3s-private-addresses/{id}. | 
**force** | **bool** | Switch to an address the server&#39;s network configuration isn&#39;t known to keep after a reboot. | [optional] 

## Example

```python
from wodby.models.switch_k3_s_server_address_input import SwitchK3SServerAddressInput

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchK3SServerAddressInput from a JSON string
switch_k3_s_server_address_input_instance = SwitchK3SServerAddressInput.from_json(json)
# print the JSON string representation of the object
print(SwitchK3SServerAddressInput.to_json())

# convert the object into a dict
switch_k3_s_server_address_input_dict = switch_k3_s_server_address_input_instance.to_dict()
# create an instance of SwitchK3SServerAddressInput from a dict
switch_k3_s_server_address_input_from_dict = SwitchK3SServerAddressInput.from_dict(switch_k3_s_server_address_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


