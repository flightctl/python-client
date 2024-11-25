# Batch

Batch is an element in batch sequence.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selector** | [**LabelSelector**](LabelSelector.md) |  | [optional] 
**success_threshold** | **str** | Percentage is the string format representing percentage string. | [optional] 
**limit** | [**BatchLimit**](BatchLimit.md) |  | [optional] 

## Example

```python
from flightctl.models.batch import Batch

# TODO update the JSON string below
json = "{}"
# create an instance of Batch from a JSON string
batch_instance = Batch.from_json(json)
# print the JSON string representation of the object
print(Batch.to_json())

# convert the object into a dict
batch_dict = batch_instance.to_dict()
# create an instance of Batch from a dict
batch_from_dict = Batch.from_dict(batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


