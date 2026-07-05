# ProblemFieldError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**detail** | **str** |  | 

## Example

```python
from wodby.models.problem_field_error import ProblemFieldError

# TODO update the JSON string below
json = "{}"
# create an instance of ProblemFieldError from a JSON string
problem_field_error_instance = ProblemFieldError.from_json(json)
# print the JSON string representation of the object
print(ProblemFieldError.to_json())

# convert the object into a dict
problem_field_error_dict = problem_field_error_instance.to_dict()
# create an instance of ProblemFieldError from a dict
problem_field_error_from_dict = ProblemFieldError.from_dict(problem_field_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


