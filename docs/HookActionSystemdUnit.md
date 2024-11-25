# HookActionSystemdUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the systemd unit on which the specified operations will be performed. This should be the exact name of the unit file, such as example.service. If the name is not populated the name will be auto discovered from the file path. | 
**operations** | **List[str]** | The specific systemd operations to perform on the specified unit. | 
**work_dir** | **str** | The directory in which the executable will be run from if it is left empty it will run from the users home directory. | [optional] 

## Example

```python
from flightctl.models.hook_action_systemd_unit import HookActionSystemdUnit

# TODO update the JSON string below
json = "{}"
# create an instance of HookActionSystemdUnit from a JSON string
hook_action_systemd_unit_instance = HookActionSystemdUnit.from_json(json)
# print the JSON string representation of the object
print(HookActionSystemdUnit.to_json())

# convert the object into a dict
hook_action_systemd_unit_dict = hook_action_systemd_unit_instance.to_dict()
# create an instance of HookActionSystemdUnit from a dict
hook_action_systemd_unit_from_dict = HookActionSystemdUnit.from_dict(hook_action_systemd_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


