# Fleet Management HTTP API Client

This is a Client for the Fleet Management HTTP API. You can find the Fleet Management HTTP API repository [here](https://gitlab.bringauto.com/bring-auto/industrial-portal/fleet-management-v2-api).
The HTTP API is described by the `openapi/openapi.yaml` according to [OpenAPI Specification](https://openapis.org).
A full specification can be found in the `openapi` folder in the root folder.

## Auto-generated code
The auto-generated code can be found in the `fleet_management_client` folder.
The code is generated using the `openapi-generator-cli` tool. The code is generated using the `openapi/openapi.yaml` file.
DO NOT edit the auto-generated code manually.

# Installation
To install the client, run
```bash
pip install git+https://github.com/bringauto/fleet-management-http-api-client.git
```

## Client re-generation
If you want to re-generate the client code with the new specification, you first have to replace the specification in the `openapi` folder.
Then you can run the `regen.sh` script (from the root folder).

# Requirements
Python 3.10.12+

# Testing
