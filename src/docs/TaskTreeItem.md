# TaskTreeItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task** | [**Task**](Task.md) |  | 
**parent_id** | **int** |  | [optional] 

## Example

```python
from wodby.models.task_tree_item import TaskTreeItem

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTreeItem from a JSON string
task_tree_item_instance = TaskTreeItem.from_json(json)
# print the JSON string representation of the object
print(TaskTreeItem.to_json())

# convert the object into a dict
task_tree_item_dict = task_tree_item_instance.to_dict()
# create an instance of TaskTreeItem from a dict
task_tree_item_from_dict = TaskTreeItem.from_dict(task_tree_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


