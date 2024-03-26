# CarState

Car State object structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**status** | [**CarStatus**](CarStatus.md) |  | 
**fuel** | **int** |  | [optional] [default to 0]
**car_id** | **int** |  | 
**speed** | **float** |  | [optional] [default to 0.0]
**position** | [**GNSSPosition**](GNSSPosition.md) |  | [optional] 

## Example

```python
from fleet_management_http_client_python.models.car_state import CarState

# TODO update the JSON string below
json = "{}"
# create an instance of CarState from a JSON string
car_state_instance = CarState.from_json(json)
# print the JSON string representation of the object
print(CarState.to_json())

# convert the object into a dict
car_state_dict = car_state_instance.to_dict()
# create an instance of CarState from a dict
car_state_form_dict = car_state.from_dict(car_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


