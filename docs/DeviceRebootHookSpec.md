# DeviceRebootHookSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**actions** | [**List[HookAction]**](HookAction.md) | The actions taken before and after system reboots are observed. Each action is executed in the order they are defined. | 

## Example

```python
from flightctl.models.device_reboot_hook_spec import DeviceRebootHookSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceRebootHookSpec from a JSON string
device_reboot_hook_spec_instance = DeviceRebootHookSpec.from_json(json)
# print the JSON string representation of the object
print(DeviceRebootHookSpec.to_json())

# convert the object into a dict
device_reboot_hook_spec_dict = device_reboot_hook_spec_instance.to_dict()
# create an instance of DeviceRebootHookSpec from a dict
device_reboot_hook_spec_from_dict = DeviceRebootHookSpec.from_dict(device_reboot_hook_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


