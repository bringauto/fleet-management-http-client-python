# PlatformHW

PlatformHW object structure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from fleet-management-http-client-python.models.platform_hw import PlatformHW

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformHW from a JSON string
platform_hw_instance = PlatformHW.from_json(json)
# print the JSON string representation of the object
print(PlatformHW.to_json())

# convert the object into a dict
platform_hw_dict = platform_hw_instance.to_dict()
# create an instance of PlatformHW from a dict
platform_hw_form_dict = platform_hw.from_dict(platform_hw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


