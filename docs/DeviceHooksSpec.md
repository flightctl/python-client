# DeviceHooksSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**before_updating** | [**List[DeviceUpdateHookSpec]**](DeviceUpdateHookSpec.md) | Hooks executed before updating allow for custom actions and integration with other systems or services. These actions occur before configuration changes are applied to the device.  | [optional] 
**after_updating** | [**List[DeviceUpdateHookSpec]**](DeviceUpdateHookSpec.md) | Hooks executed after updating enable custom actions and integration with other systems or services. These actions occur after configuration changes have been applied to the device.  | [optional] 
**before_rebooting** | [**List[DeviceRebootHookSpec]**](DeviceRebootHookSpec.md) | Hooks executed before rebooting allow for custom actions and integration with other systems or services. These actions occur before the device is rebooted.  | [optional] 
**after_rebooting** | [**List[DeviceRebootHookSpec]**](DeviceRebootHookSpec.md) | Hooks executed after rebooting enable custom actions and integration with other systems or services. These actions occur after the device has rebooted, allowing for post-reboot tasks.  | [optional] 

## Example

```python
from flightctl.models.device_hooks_spec import DeviceHooksSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceHooksSpec from a JSON string
device_hooks_spec_instance = DeviceHooksSpec.from_json(json)
# print the JSON string representation of the object
print(DeviceHooksSpec.to_json())

# convert the object into a dict
device_hooks_spec_dict = device_hooks_spec_instance.to_dict()
# create an instance of DeviceHooksSpec from a dict
device_hooks_spec_from_dict = DeviceHooksSpec.from_dict(device_hooks_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


