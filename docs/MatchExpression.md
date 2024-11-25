# MatchExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**operator** | **str** |  | 
**values** | **List[str]** |  | [optional] 

## Example

```python
from flightctl.models.match_expression import MatchExpression

# TODO update the JSON string below
json = "{}"
# create an instance of MatchExpression from a JSON string
match_expression_instance = MatchExpression.from_json(json)
# print the JSON string representation of the object
print(MatchExpression.to_json())

# convert the object into a dict
match_expression_dict = match_expression_instance.to_dict()
# create an instance of MatchExpression from a dict
match_expression_from_dict = MatchExpression.from_dict(match_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


