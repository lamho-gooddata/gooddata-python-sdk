# gooddata-scan-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v0
- Package version: 1.1.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import gooddata_scan_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import gooddata_scan_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import gooddata_scan_client
from pprint import pprint
from gooddata_scan_client.api import actions_api
from gooddata_scan_client.model.data_source_schemata import DataSourceSchemata
from gooddata_scan_client.model.scan_request import ScanRequest
from gooddata_scan_client.model.scan_result_pdm import ScanResultPdm
from gooddata_scan_client.model.test_definition_request import TestDefinitionRequest
from gooddata_scan_client.model.test_request import TestRequest
from gooddata_scan_client.model.test_response import TestResponse
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gooddata_scan_client.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with gooddata_scan_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = actions_api.ActionsApi(api_client)
    data_source_id = "myPostgres" # str | Data source id

    try:
        # Get a list of schema names of a database
        api_response = api_instance.get_data_source_schemata(data_source_id)
        pprint(api_response)
    except gooddata_scan_client.ApiException as e:
        print("Exception when calling ActionsApi->get_data_source_schemata: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ActionsApi* | [**get_data_source_schemata**](docs/ActionsApi.md#get_data_source_schemata) | **GET** /api/v1/actions/dataSources/{dataSourceId}/scanSchemata | Get a list of schema names of a database
*ActionsApi* | [**scan_data_source**](docs/ActionsApi.md#scan_data_source) | **POST** /api/v1/actions/dataSources/{dataSourceId}/scan | Scan a database to get a physical data model (PDM)
*ActionsApi* | [**test_data_source**](docs/ActionsApi.md#test_data_source) | **POST** /api/v1/actions/dataSources/{dataSourceId}/test | Test data source connection by data source id
*ActionsApi* | [**test_data_source_definition**](docs/ActionsApi.md#test_data_source_definition) | **POST** /api/v1/actions/dataSource/test | Test connection by data source definition


## Documentation For Models

 - [ColumnWarning](docs/ColumnWarning.md)
 - [DataSourceParameter](docs/DataSourceParameter.md)
 - [DataSourceSchemata](docs/DataSourceSchemata.md)
 - [DeclarativeColumn](docs/DeclarativeColumn.md)
 - [DeclarativeTable](docs/DeclarativeTable.md)
 - [DeclarativeTables](docs/DeclarativeTables.md)
 - [ScanRequest](docs/ScanRequest.md)
 - [ScanResultPdm](docs/ScanResultPdm.md)
 - [TableWarning](docs/TableWarning.md)
 - [TestDefinitionRequest](docs/TestDefinitionRequest.md)
 - [TestRequest](docs/TestRequest.md)
 - [TestResponse](docs/TestResponse.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author

support@gooddata.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in gooddata_scan_client.apis and gooddata_scan_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from gooddata_scan_client.api.default_api import DefaultApi`
- `from gooddata_scan_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import gooddata_scan_client
from gooddata_scan_client.apis import *
from gooddata_scan_client.models import *
```

