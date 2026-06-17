# URLResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 

## Example

```python
from wodby.models.url_response import URLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of URLResponse from a JSON string
url_response_instance = URLResponse.from_json(json)
# print the JSON string representation of the object
print(URLResponse.to_json())

# convert the object into a dict
url_response_dict = url_response_instance.to_dict()
# create an instance of URLResponse from a dict
url_response_from_dict = URLResponse.from_dict(url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


