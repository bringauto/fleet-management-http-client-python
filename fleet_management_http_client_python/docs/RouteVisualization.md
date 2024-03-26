# RouteVisualization

Route Visualization object structure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**route_id** | **int** |  | 
**hexcolor** | **str** | Color in hexadecimal format. | [optional] [default to '#FF0000']
**points** | [**List[GNSSPosition]**](GNSSPosition.md) |  | [default to []]

## Example

```python
from fleet_management_http_client_python.models.route_visualization import RouteVisualization

# TODO update the JSON string below
json = "{}"
# create an instance of RouteVisualization from a JSON string
route_visualization_instance = RouteVisualization.from_json(json)
# print the JSON string representation of the object
print(RouteVisualization.to_json())

# convert the object into a dict
route_visualization_dict = route_visualization_instance.to_dict()
# create an instance of RouteVisualization from a dict
route_visualization_form_dict = route_visualization.from_dict(route_visualization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


