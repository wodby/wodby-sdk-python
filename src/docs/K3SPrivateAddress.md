# K3SPrivateAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**network_interface** | **str** | The network interface the address is on, such as enp0s31f6.4000 for a VLAN. | 
**mtu** | **int** | The interface&#39;s MTU, or 0 when the server doesn&#39;t report it. | 
**persistent** | **bool** | Whether the server&#39;s network configuration brings the address back after a reboot. k3s doesn&#39;t start when its address is gone, so switching to an address that isn&#39;t persistent needs force. | 
**persistent_source** | **str** | What keeps the address after a reboot, such as systemd-networkd or NetworkManager. | [optional] 

## Example

```python
from wodby.models.k3_s_private_address import K3SPrivateAddress

# TODO update the JSON string below
json = "{}"
# create an instance of K3SPrivateAddress from a JSON string
k3_s_private_address_instance = K3SPrivateAddress.from_json(json)
# print the JSON string representation of the object
print(K3SPrivateAddress.to_json())

# convert the object into a dict
k3_s_private_address_dict = k3_s_private_address_instance.to_dict()
# create an instance of K3SPrivateAddress from a dict
k3_s_private_address_from_dict = K3SPrivateAddress.from_dict(k3_s_private_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


