# fleet_management_http_client_python.CarActionApi

All URIs are relative to */v2/management*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_car_action_states**](CarActionApi.md#get_car_action_states) | **GET** /action/car/{carId} | Finds car action states for a Car with given carId.
[**pause_car**](CarActionApi.md#pause_car) | **POST** /action/car/{carId}/pause | Finds and pauses a Car with given carId, if not already paused. Sets car action status to PAUSED if it is not in PAUSED action status already.
[**unpause_car**](CarActionApi.md#unpause_car) | **POST** /action/car/{carId}/unpause | Finds and unpauses a Car with given carId, if paused. Sets car action status to NORMAL only if it is in PAUSED action status.


# **get_car_action_states**
> List[CarActionState] get_car_action_states(car_id, wait=wait, since=since, last_n=last_n)

Finds car action states for a Car with given carId.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet_management_http_client_python
from fleet_management_http_client_python.models.car_action_state import CarActionState
from fleet_management_http_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet_management_http_client_python.Configuration(
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
with fleet_management_http_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet_management_http_client_python.CarActionApi(api_client)
    car_id = 1 # int | ID of the Car for which to return the action states.
    wait = False # bool | Applies to GET methods when no objects would be returned at the moment of request. If wait=true, \\ the request will wait for the next object to be created and then returns it. If wait=False or unspecified, the request will return \\ an empty list. (optional) (default to False)
    since = 56 # int | A Unix timestamp in milliseconds. If specified, only objects created at the time or later will be returned. If unspecified, all objects are returned (since is set to 0 in that case). (optional)
    last_n = 0 # int | If specified, only the last N objects will be returned. If unspecified, all objects are returned. \\ If some states have identical timestamps and they all do not fit into the maximum N states, only those with higher IDs are returned. If value smaller than 1 is provided, this filtering is ignored. (optional) (default to 0)

    try:
        # Finds car action states for a Car with given carId.
        api_response = api_instance.get_car_action_states(car_id, wait=wait, since=since, last_n=last_n)
        print("The response of CarActionApi->get_car_action_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarActionApi->get_car_action_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**| ID of the Car for which to return the action states. | 
 **wait** | **bool**| Applies to GET methods when no objects would be returned at the moment of request. If wait&#x3D;true, \\ the request will wait for the next object to be created and then returns it. If wait&#x3D;False or unspecified, the request will return \\ an empty list. | [optional] [default to False]
 **since** | **int**| A Unix timestamp in milliseconds. If specified, only objects created at the time or later will be returned. If unspecified, all objects are returned (since is set to 0 in that case). | [optional] 
 **last_n** | **int**| If specified, only the last N objects will be returned. If unspecified, all objects are returned. \\ If some states have identical timestamps and they all do not fit into the maximum N states, only those with higher IDs are returned. If value smaller than 1 is provided, this filtering is ignored. | [optional] [default to 0]

### Return type

[**List[CarActionState]**](CarActionState.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully found Car Action States complying with the request parameters. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_car**
> List[CarActionState] pause_car(car_id)

Finds and pauses a Car with given carId, if not already paused. Sets car action status to PAUSED if it is not in PAUSED action status already.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet_management_http_client_python
from fleet_management_http_client_python.models.car_action_state import CarActionState
from fleet_management_http_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet_management_http_client_python.Configuration(
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
with fleet_management_http_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet_management_http_client_python.CarActionApi(api_client)
    car_id = 1 # int | ID of the Car which should be paused.

    try:
        # Finds and pauses a Car with given carId, if not already paused. Sets car action status to PAUSED if it is not in PAUSED action status already.
        api_response = api_instance.pause_car(car_id)
        print("The response of CarActionApi->pause_car:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarActionApi->pause_car: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**| ID of the Car which should be paused. | 

### Return type

[**List[CarActionState]**](CarActionState.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully paused the Car. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpause_car**
> List[CarActionState] unpause_car(car_id)

Finds and unpauses a Car with given carId, if paused. Sets car action status to NORMAL only if it is in PAUSED action status.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet_management_http_client_python
from fleet_management_http_client_python.models.car_action_state import CarActionState
from fleet_management_http_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet_management_http_client_python.Configuration(
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
with fleet_management_http_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet_management_http_client_python.CarActionApi(api_client)
    car_id = 1 # int | ID of the Car which should be unpaused.

    try:
        # Finds and unpauses a Car with given carId, if paused. Sets car action status to NORMAL only if it is in PAUSED action status.
        api_response = api_instance.unpause_car(car_id)
        print("The response of CarActionApi->unpause_car:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarActionApi->unpause_car: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**| ID of the Car which should be unpaused. | 

### Return type

[**List[CarActionState]**](CarActionState.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully unpaused the Car. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

