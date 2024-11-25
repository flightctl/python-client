# HookActionSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout** | **str** | The maximum duration allowed for the action to complete. The duration should be specified as a positive integer followed by a time unit. Supported time units are: - &#39;s&#39; for seconds - &#39;m&#39; for minutes - &#39;h&#39; for hours - &#39;d&#39; for days  | [optional] 

## Example

```python
from flightctl.models.hook_action_spec import HookActionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HookActionSpec from a JSON string
hook_action_spec_instance = HookActionSpec.from_json(json)
# print the JSON string representation of the object
print(HookActionSpec.to_json())

# convert the object into a dict
hook_action_spec_dict = hook_action_spec_instance.to_dict()
# create an instance of HookActionSpec from a dict
hook_action_spec_from_dict = HookActionSpec.from_dict(hook_action_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


