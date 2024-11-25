# HookActionSystemdSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout** | **str** | The maximum duration allowed for the action to complete. The duration should be specified as a positive integer followed by a time unit. Supported time units are: - &#39;s&#39; for seconds - &#39;m&#39; for minutes - &#39;h&#39; for hours - &#39;d&#39; for days  | [optional] 
**unit** | [**HookActionSystemdUnit**](HookActionSystemdUnit.md) |  | 

## Example

```python
from flightctl.models.hook_action_systemd_spec import HookActionSystemdSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HookActionSystemdSpec from a JSON string
hook_action_systemd_spec_instance = HookActionSystemdSpec.from_json(json)
# print the JSON string representation of the object
print(HookActionSystemdSpec.to_json())

# convert the object into a dict
hook_action_systemd_spec_dict = hook_action_systemd_spec_instance.to_dict()
# create an instance of HookActionSystemdSpec from a dict
hook_action_systemd_spec_from_dict = HookActionSystemdSpec.from_dict(hook_action_systemd_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


