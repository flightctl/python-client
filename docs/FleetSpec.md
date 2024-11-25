# FleetSpec

FleetSpec is a description of a fleet's target state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selector** | [**LabelSelector**](LabelSelector.md) |  | [optional] 
**rollout_policy** | [**RolloutPolicy**](RolloutPolicy.md) |  | [optional] 
**template** | [**FleetSpecTemplate**](FleetSpecTemplate.md) |  | 

## Example

```python
from flightctl.models.fleet_spec import FleetSpec

# TODO update the JSON string below
json = "{}"
# create an instance of FleetSpec from a JSON string
fleet_spec_instance = FleetSpec.from_json(json)
# print the JSON string representation of the object
print(FleetSpec.to_json())

# convert the object into a dict
fleet_spec_dict = fleet_spec_instance.to_dict()
# create an instance of FleetSpec from a dict
fleet_spec_from_dict = FleetSpec.from_dict(fleet_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


