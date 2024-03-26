# fleet-management-http-client-python.RouteApi

All URIs are relative to */v2/management*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_route**](RouteApi.md#create_route) | **POST** /route | Create a new Route.
[**delete_route**](RouteApi.md#delete_route) | **DELETE** /route/{routeId} | Delete a Route with the specified ID.
[**get_route**](RouteApi.md#get_route) | **GET** /route/{routeId} | Find a single Route with the specified ID.
[**get_route_visualization**](RouteApi.md#get_route_visualization) | **GET** /route-visualization/{routeId} | Find Route Visualization for a Route identified by the route&#39;s ID.
[**get_routes**](RouteApi.md#get_routes) | **GET** /route | Find and return all existing Routes.
[**redefine_route_visualization**](RouteApi.md#redefine_route_visualization) | **POST** /route-visualization | Redefine Route Visualization for an existing Route.
[**update_route**](RouteApi.md#update_route) | **PUT** /route | Update already existing Route.


# **create_route**
> Route create_route(route)

Create a new Route.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet-management-http-client-python
from fleet-management-http-client-python.models.route import Route
from fleet-management-http-client-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet-management-http-client-python.Configuration(
    host = "/v2/management"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIKeyAuth
configuration.api_key['APIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with fleet-management-http-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet-management-http-client-python.RouteApi(api_client)
    route = fleet-management-http-client-python.Route() # Route | Route model in JSON format.

    try:
        # Create a new Route.
        api_response = api_instance.create_route(route)
        print("The response of RouteApi->create_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteApi->create_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route** | [**Route**](Route.md)| Route model in JSON format. | 

### Return type

[**Route**](Route.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Route has been successfully created. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_route**
> delete_route(route_id)

Delete a Route with the specified ID.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet-management-http-client-python
from fleet-management-http-client-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet-management-http-client-python.Configuration(
    host = "/v2/management"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIKeyAuth
configuration.api_key['APIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with fleet-management-http-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet-management-http-client-python.RouteApi(api_client)
    route_id = 1 # int | An ID a the Route

    try:
        # Delete a Route with the specified ID.
        api_instance.delete_route(route_id)
    except Exception as e:
        print("Exception when calling RouteApi->delete_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **int**| An ID a the Route | 

### Return type

void (empty response body)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Route with the specified ID has been deleted. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**405** | Method not allowed |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route**
> Route get_route(route_id)

Find a single Route with the specified ID.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet-management-http-client-python
from fleet-management-http-client-python.models.route import Route
from fleet-management-http-client-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet-management-http-client-python.Configuration(
    host = "/v2/management"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIKeyAuth
configuration.api_key['APIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with fleet-management-http-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet-management-http-client-python.RouteApi(api_client)
    route_id = 1 # int | An ID a the Route

    try:
        # Find a single Route with the specified ID.
        api_response = api_instance.get_route(route_id)
        print("The response of RouteApi->get_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteApi->get_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **int**| An ID a the Route | 

### Return type

[**Route**](Route.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Route with the specified ID has been found and returned. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_visualization**
> RouteVisualization get_route_visualization(route_id)

Find Route Visualization for a Route identified by the route's ID.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet-management-http-client-python
from fleet-management-http-client-python.models.route_visualization import RouteVisualization
from fleet-management-http-client-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet-management-http-client-python.Configuration(
    host = "/v2/management"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIKeyAuth
configuration.api_key['APIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with fleet-management-http-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet-management-http-client-python.RouteApi(api_client)
    route_id = 1 # int | An ID a the Route

    try:
        # Find Route Visualization for a Route identified by the route's ID.
        api_response = api_instance.get_route_visualization(route_id)
        print("The response of RouteApi->get_route_visualization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteApi->get_route_visualization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **int**| An ID a the Route | 

### Return type

[**RouteVisualization**](RouteVisualization.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Route Visualization for the specified Route ID has been found and returned. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routes**
> List[Route] get_routes()

Find and return all existing Routes.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet-management-http-client-python
from fleet-management-http-client-python.models.route import Route
from fleet-management-http-client-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet-management-http-client-python.Configuration(
    host = "/v2/management"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIKeyAuth
configuration.api_key['APIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with fleet-management-http-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet-management-http-client-python.RouteApi(api_client)

    try:
        # Find and return all existing Routes.
        api_response = api_instance.get_routes()
        print("The response of RouteApi->get_routes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteApi->get_routes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Route]**](Route.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All the currently existing Routes have been returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redefine_route_visualization**
> redefine_route_visualization(route_visualization)

Redefine Route Visualization for an existing Route.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet-management-http-client-python
from fleet-management-http-client-python.models.route_visualization import RouteVisualization
from fleet-management-http-client-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet-management-http-client-python.Configuration(
    host = "/v2/management"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIKeyAuth
configuration.api_key['APIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with fleet-management-http-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet-management-http-client-python.RouteApi(api_client)
    route_visualization = fleet-management-http-client-python.RouteVisualization() # RouteVisualization | Route Visualization model in JSON format.

    try:
        # Redefine Route Visualization for an existing Route.
        api_instance.redefine_route_visualization(route_visualization)
    except Exception as e:
        print("Exception when calling RouteApi->redefine_route_visualization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_visualization** | [**RouteVisualization**](RouteVisualization.md)| Route Visualization model in JSON format. | 

### Return type

void (empty response body)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Route Visualization has been successfully redefined. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_route**
> update_route(route)

Update already existing Route.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet-management-http-client-python
from fleet-management-http-client-python.models.route import Route
from fleet-management-http-client-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet-management-http-client-python.Configuration(
    host = "/v2/management"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIKeyAuth
configuration.api_key['APIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with fleet-management-http-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet-management-http-client-python.RouteApi(api_client)
    route = fleet-management-http-client-python.Route() # Route | JSON representation of the updated Route.

    try:
        # Update already existing Route.
        api_instance.update_route(route)
    except Exception as e:
        print("Exception when calling RouteApi->update_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route** | [**Route**](Route.md)| JSON representation of the updated Route. | 

### Return type

void (empty response body)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Route has been successfully updated. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

