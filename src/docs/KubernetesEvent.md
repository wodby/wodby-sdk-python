# KubernetesEvent

A Kubernetes event in an app environment, with repeats of the same event merged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Warning or Normal. | 
**reason** | **str** |  | 
**message** | **str** | The event&#39;s message with known secret values masked. | 
**object_kind** | **str** | Kind of the object the event is about, such as Pod or PersistentVolumeClaim. | 
**object_name** | **str** |  | 
**app_service_id** | **int** | The app service the object belongs to. Null for objects no app service defines, or ones Wodby can&#39;t attribute. | 
**source** | **str** | The component that reported the event, such as kubelet or default-scheduler. | 
**count** | **int** | How many times the event occurred. | 
**first_seen** | **datetime** |  | 
**last_seen** | **datetime** |  | 

## Example

```python
from wodby.models.kubernetes_event import KubernetesEvent

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesEvent from a JSON string
kubernetes_event_instance = KubernetesEvent.from_json(json)
# print the JSON string representation of the object
print(KubernetesEvent.to_json())

# convert the object into a dict
kubernetes_event_dict = kubernetes_event_instance.to_dict()
# create an instance of KubernetesEvent from a dict
kubernetes_event_from_dict = KubernetesEvent.from_dict(kubernetes_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


