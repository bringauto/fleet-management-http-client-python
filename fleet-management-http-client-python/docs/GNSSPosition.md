# GNSSPosition

GNSSPosition primitive structure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** |  | [optional] [default to 0.0]
**longitude** | **float** |  | [optional] [default to 0.0]
**altitude** | **float** |  | [optional] [default to 0.0]

## Example

```python
from fleet-management-http-client-python.models.gnss_position import GNSSPosition

# TODO update the JSON string below
json = "{}"
# create an instance of GNSSPosition from a JSON string
gnss_position_instance = GNSSPosition.from_json(json)
# print the JSON string representation of the object
print(GNSSPosition.to_json())

# convert the object into a dict
gnss_position_dict = gnss_position_instance.to_dict()
# create an instance of GNSSPosition from a dict
gnss_position_form_dict = gnss_position.from_dict(gnss_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


