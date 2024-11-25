# HookActionExecutable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run** | **str** | The command to be executed, including any arguments using standard shell syntax. This field supports multiple commands piped together, as if they were executed under a bash -c context. | 
**env_vars** | **List[str]** | An optional list of KEY&#x3D;VALUE pairs to set as environment variables for the executable. | [optional] 
**work_dir** | **str** | The directory in which the executable will be run from if it is left empty it will run from the users home directory. | [optional] 

## Example

```python
from flightctl.models.hook_action_executable import HookActionExecutable

# TODO update the JSON string below
json = "{}"
# create an instance of HookActionExecutable from a JSON string
hook_action_executable_instance = HookActionExecutable.from_json(json)
# print the JSON string representation of the object
print(HookActionExecutable.to_json())

# convert the object into a dict
hook_action_executable_dict = hook_action_executable_instance.to_dict()
# create an instance of HookActionExecutable from a dict
hook_action_executable_from_dict = HookActionExecutable.from_dict(hook_action_executable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


