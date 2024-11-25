# DisruptionAllowance

DisruptionAllowance defines the level of allowed disruption when rollout is in progress.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | **List[str]** | List of label keys to perform grouping for the disruption allowance. | [optional] 
**min_available** | **int** | The maximum number of unavailable devices allowed during rollout. | [optional] 
**max_unavailable** | **int** | The minimum number of required available devices during rollout. | [optional] 

## Example

```python
from flightctl.models.disruption_allowance import DisruptionAllowance

# TODO update the JSON string below
json = "{}"
# create an instance of DisruptionAllowance from a JSON string
disruption_allowance_instance = DisruptionAllowance.from_json(json)
# print the JSON string representation of the object
print(DisruptionAllowance.to_json())

# convert the object into a dict
disruption_allowance_dict = disruption_allowance_instance.to_dict()
# create an instance of DisruptionAllowance from a dict
disruption_allowance_from_dict = DisruptionAllowance.from_dict(disruption_allowance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


