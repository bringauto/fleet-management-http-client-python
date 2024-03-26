#!/bin/bash

npx @openapitools/openapi-generator-cli generate -i openapi/openapi.yaml \
 --generator-name python \
 --output . \
 --package-name fleet_management_http_client_python \
 --additional-properties=generateSourceCodeOnly=true,apiTests=false,modelTests=false