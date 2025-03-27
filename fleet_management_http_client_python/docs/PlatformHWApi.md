# fleet_management_http_client_python.PlatformHWApi

All URIs are relative to */v2/management*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hws**](PlatformHWApi.md#create_hws) | **POST** /platformhw | Create new Platform HW objects.
[**delete_hw**](PlatformHWApi.md#delete_hw) | **DELETE** /platformhw/{platformHwId} | Delete Platform HW with the given ID.
[**get_hw**](PlatformHWApi.md#get_hw) | **GET** /platformhw/{platformHwId} | Find Platform HW with the given ID.
[**get_hws**](PlatformHWApi.md#get_hws) | **GET** /platformhw | Find and return all existing Platform HW.


# **create_hws**
> List[PlatformHW] create_hws(platform_hw)

Create new Platform HW objects.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet_management_http_client_python
from fleet_management_http_client_python.models.platform_hw import PlatformHW
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
    api_instance = fleet_management_http_client_python.PlatformHWApi(api_client)
    platform_hw = [fleet_management_http_client_python.PlatformHW()] # List[PlatformHW] | A list of Platform HW models in JSON format.

    try:
        # Create new Platform HW objects.
        api_response = api_instance.create_hws(platform_hw)
        print("The response of PlatformHWApi->create_hws:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformHWApi->create_hws: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_hw** | [**List[PlatformHW]**](PlatformHW.md)| A list of Platform HW models in JSON format. | 

### Return type

[**List[PlatformHW]**](PlatformHW.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Platform HWs have been successfully created. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hw**
> delete_hw(platform_hw_id)

Delete Platform HW with the given ID.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet_management_http_client_python
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
    api_instance = fleet_management_http_client_python.PlatformHWApi(api_client)
    platform_hw_id = 56 # int | The Platform HW ID.

    try:
        # Delete Platform HW with the given ID.
        api_instance.delete_hw(platform_hw_id)
    except Exception as e:
        print("Exception when calling PlatformHWApi->delete_hw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_hw_id** | **int**| The Platform HW ID. | 

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
**200** | The Platform HW with the specified ID has been deleted. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**405** | Method not allowed |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hw**
> PlatformHW get_hw(platform_hw_id)

Find Platform HW with the given ID.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet_management_http_client_python
from fleet_management_http_client_python.models.platform_hw import PlatformHW
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
    api_instance = fleet_management_http_client_python.PlatformHWApi(api_client)
    platform_hw_id = 56 # int | The Platform HW ID.

    try:
        # Find Platform HW with the given ID.
        api_response = api_instance.get_hw(platform_hw_id)
        print("The response of PlatformHWApi->get_hw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformHWApi->get_hw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_hw_id** | **int**| The Platform HW ID. | 

### Return type

[**PlatformHW**](PlatformHW.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Platform HW with the specified ID has been found and returned. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hws**
> List[PlatformHW] get_hws()

Find and return all existing Platform HW.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet_management_http_client_python
from fleet_management_http_client_python.models.platform_hw import PlatformHW
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
    api_instance = fleet_management_http_client_python.PlatformHWApi(api_client)

    try:
        # Find and return all existing Platform HW.
        api_response = api_instance.get_hws()
        print("The response of PlatformHWApi->get_hws:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformHWApi->get_hws: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PlatformHW]**](PlatformHW.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All the currently existing Platform HWs have been returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

