# DeviceUpdateHookSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**actions** | [**List[HookAction]**](HookAction.md) | The actions to take when the specified file operations are observed. Each action is executed in the order they are defined. | 
**on_file** | [**List[FileOperation]**](FileOperation.md) |  | [optional] 
**path** | **str** | The path to monitor for changes in configuration files. This path can point to either a specific file or an entire directory. | [optional] 

## Example

```python
from flightctl.models.device_update_hook_spec import DeviceUpdateHookSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUpdateHookSpec from a JSON string
device_update_hook_spec_instance = DeviceUpdateHookSpec.from_json(json)
# print the JSON string representation of the object
print(DeviceUpdateHookSpec.to_json())

# convert the object into a dict
device_update_hook_spec_dict = device_update_hook_spec_instance.to_dict()
# create an instance of DeviceUpdateHookSpec from a dict
device_update_hook_spec_from_dict = DeviceUpdateHookSpec.from_dict(device_update_hook_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


