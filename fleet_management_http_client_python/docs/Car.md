# Car

Car model structure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**platform_hw_id** | **int** |  | 
**name** | **str** |  | 
**car_admin_phone** | [**MobilePhone**](MobilePhone.md) |  | 
**default_route_id** | **int** |  | [optional] 
**under_test** | **bool** |  | [optional] [default to True]
**last_state** | [**CarState**](CarState.md) |  | [optional] 
**last_action_state** | [**CarActionState**](CarActionState.md) |  | [optional] 

## Example

```python
from fleet_management_http_client_python.models.car import Car

# TODO update the JSON string below
json = "{}"
# create an instance of Car from a JSON string
car_instance = Car.from_json(json)
# print the JSON string representation of the object
print(Car.to_json())

# convert the object into a dict
car_dict = car_instance.to_dict()
# create an instance of Car from a dict
car_form_dict = car.from_dict(car_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


