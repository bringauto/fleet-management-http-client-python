# fleet_management_http_client_python.ApiApi

All URIs are relative to */v2/management*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_api_is_alive**](ApiApi.md#check_api_is_alive) | **HEAD** /apialive | Check HTTP server is running and accessible.


# **check_api_is_alive**
> check_api_is_alive()

Check HTTP server is running and accessible.

### Example


```python
import fleet_management_http_client_python
from fleet_management_http_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet_management_http_client_python.Configuration(
    host = "/v2/management"
)


# Enter a context with an instance of the API client
with fleet_management_http_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet_management_http_client_python.ApiApi(api_client)

    try:
        # Check HTTP server is running and accessible.
        api_instance.check_api_is_alive()
    except Exception as e:
        print("Exception when calling ApiApi->check_api_is_alive: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP server has been reached successfully. |  -  |
**503** | Service unavailable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

