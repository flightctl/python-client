# HookActionExecutableSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout** | **str** | The maximum duration allowed for the action to complete. The duration should be specified as a positive integer followed by a time unit. Supported time units are: - &#39;s&#39; for seconds - &#39;m&#39; for minutes - &#39;h&#39; for hours - &#39;d&#39; for days  | [optional] 
**run** | **str** | The command to be executed, including any arguments using standard shell syntax. This field supports multiple commands piped together, as if they were executed under a bash -c context. | 
**env_vars** | **List[str]** | An optional list of KEY&#x3D;VALUE pairs to set as environment variables for the executable. | [optional] 
**work_dir** | **str** | The directory in which the executable will be run from if it is left empty it will run from the users home directory. | [optional] 

## Example

```python
from flightctl.models.hook_action_executable_spec import HookActionExecutableSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HookActionExecutableSpec from a JSON string
hook_action_executable_spec_instance = HookActionExecutableSpec.from_json(json)
# print the JSON string representation of the object
print(HookActionExecutableSpec.to_json())

# convert the object into a dict
hook_action_executable_spec_dict = hook_action_executable_spec_instance.to_dict()
# create an instance of HookActionExecutableSpec from a dict
hook_action_executable_spec_from_dict = HookActionExecutableSpec.from_dict(hook_action_executable_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


