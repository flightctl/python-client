# HookAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executable** | [**HookActionExecutableSpec**](HookActionExecutableSpec.md) |  | 
**systemd** | [**HookActionSystemdSpec**](HookActionSystemdSpec.md) |  | 

## Example

```python
from flightctl.models.hook_action import HookAction

# TODO update the JSON string below
json = "{}"
# create an instance of HookAction from a JSON string
hook_action_instance = HookAction.from_json(json)
# print the JSON string representation of the object
print(HookAction.to_json())

# convert the object into a dict
hook_action_dict = hook_action_instance.to_dict()
# create an instance of HookAction from a dict
hook_action_from_dict = HookAction.from_dict(hook_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


