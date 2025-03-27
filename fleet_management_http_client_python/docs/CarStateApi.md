# fleet_management_http_client_python.CarStateApi

All URIs are relative to */v2/management*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_car_states**](CarStateApi.md#create_car_states) | **POST** /carstate | Add new Car States.
[**get_all_car_states**](CarStateApi.md#get_all_car_states) | **GET** /carstate | Find one or all Car States for all existing Cars.
[**get_car_states**](CarStateApi.md#get_car_states) | **GET** /carstate/{carId} | Find one or all Car States for a Car with given ID.


# **create_car_states**
> create_car_states(car_state)

Add new Car States.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet_management_http_client_python
from fleet_management_http_client_python.models.car_state import CarState
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
    api_instance = fleet_management_http_client_python.CarStateApi(api_client)
    car_state = [fleet_management_http_client_python.CarState()] # List[CarState] | A list of Car State model in JSON format.

    try:
        # Add new Car States.
        api_instance.create_car_states(car_state)
    except Exception as e:
        print("Exception when calling CarStateApi->create_car_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_state** | [**List[CarState]**](CarState.md)| A list of Car State model in JSON format. | 

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
**200** | The new Car States have been successfully added. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_car_states**
> List[CarState] get_all_car_states(wait=wait, since=since, last_n=last_n)

Find one or all Car States for all existing Cars.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet_management_http_client_python
from fleet_management_http_client_python.models.car_state import CarState
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
    api_instance = fleet_management_http_client_python.CarStateApi(api_client)
    wait = False # bool | Applies to GET methods when no objects would be returned at the moment of request. If wait=true, \\ the request will wait for the next object to be created and then returns it. If wait=False or unspecified, the request will return \\ an empty list. (optional) (default to False)
    since = 56 # int | A Unix timestamp in milliseconds. If specified, only objects created at the time or later will be returned. If unspecified, all objects are returned (since is set to 0 in that case). (optional)
    last_n = 0 # int | If specified, only the last N objects will be returned. If unspecified, all objects are returned. \\ If some states have identical timestamps and they all do not fit into the maximum N states, only those with higher IDs are returned. If value smaller than 1 is provided, this filtering is ignored. (optional) (default to 0)

    try:
        # Find one or all Car States for all existing Cars.
        api_response = api_instance.get_all_car_states(wait=wait, since=since, last_n=last_n)
        print("The response of CarStateApi->get_all_car_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarStateApi->get_all_car_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wait** | **bool**| Applies to GET methods when no objects would be returned at the moment of request. If wait&#x3D;true, \\ the request will wait for the next object to be created and then returns it. If wait&#x3D;False or unspecified, the request will return \\ an empty list. | [optional] [default to False]
 **since** | **int**| A Unix timestamp in milliseconds. If specified, only objects created at the time or later will be returned. If unspecified, all objects are returned (since is set to 0 in that case). | [optional] 
 **last_n** | **int**| If specified, only the last N objects will be returned. If unspecified, all objects are returned. \\ If some states have identical timestamps and they all do not fit into the maximum N states, only those with higher IDs are returned. If value smaller than 1 is provided, this filtering is ignored. | [optional] [default to 0]

### Return type

[**List[CarState]**](CarState.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully found all Car States complying with the request parameters. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_car_states**
> List[CarState] get_car_states(car_id, wait=wait, since=since, last_n=last_n)

Find one or all Car States for a Car with given ID.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet_management_http_client_python
from fleet_management_http_client_python.models.car_state import CarState
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
    api_instance = fleet_management_http_client_python.CarStateApi(api_client)
    car_id = 56 # int | The car ID.
    wait = False # bool | Applies to GET methods when no objects would be returned at the moment of request. If wait=true, \\ the request will wait for the next object to be created and then returns it. If wait=False or unspecified, the request will return \\ an empty list. (optional) (default to False)
    since = 56 # int | A Unix timestamp in milliseconds. If specified, only objects created at the time or later will be returned. If unspecified, all objects are returned (since is set to 0 in that case). (optional)
    last_n = 0 # int | If specified, only the last N objects will be returned. If unspecified, all objects are returned. \\ If some states have identical timestamps and they all do not fit into the maximum N states, only those with higher IDs are returned. If value smaller than 1 is provided, this filtering is ignored. (optional) (default to 0)

    try:
        # Find one or all Car States for a Car with given ID.
        api_response = api_instance.get_car_states(car_id, wait=wait, since=since, last_n=last_n)
        print("The response of CarStateApi->get_car_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarStateApi->get_car_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**| The car ID. | 
 **wait** | **bool**| Applies to GET methods when no objects would be returned at the moment of request. If wait&#x3D;true, \\ the request will wait for the next object to be created and then returns it. If wait&#x3D;False or unspecified, the request will return \\ an empty list. | [optional] [default to False]
 **since** | **int**| A Unix timestamp in milliseconds. If specified, only objects created at the time or later will be returned. If unspecified, all objects are returned (since is set to 0 in that case). | [optional] 
 **last_n** | **int**| If specified, only the last N objects will be returned. If unspecified, all objects are returned. \\ If some states have identical timestamps and they all do not fit into the maximum N states, only those with higher IDs are returned. If value smaller than 1 is provided, this filtering is ignored. | [optional] [default to 0]

### Return type

[**List[CarState]**](CarState.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully found all Car States complying with the request parameters. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

