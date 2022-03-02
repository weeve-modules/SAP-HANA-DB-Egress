# SAP HANA Database Egress

|              |                                                                   |
| ------------ | ----------------------------------------------------------------- |
| name         | SAP HANA Database Egress                                          |
| version      | v0.0.1                                                            |
| docker image | [weevenetwork/sap-hana-database-egress](https://hub.docker.com/r/weevenetwork/sap-hana-database-egress) |
| tags         | Python, Flask, Docker, Weeve                                      |
| authors      | Sanyam Arya                                                       |

***
## Table of Content
- [SAP HANA Database Egress](#sap-hana-database-egress)
  - [Table of Content](#table-of-content)
  - [Description](#description)
    - [Features](#features)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Directory Structure](#directory-structure)
    - [File Tree](#file-tree)
  - [As a module developer](#as-a-module-developer)
    - [Configuration](#configuration)
    - [Business Logic](#business-logic)
  - [Dependencies](#dependencies)
  - [Examples](#examples)
    - [Input](#input)
    - [Output](#output)
  - [Docker Compose Example](#docker-compose-example)

***

## Description 

This module allows to save data in a selected SAP HANA Database Scheme and Table. Currently this module supports only AMD architecture.

### Features
1. Flask ReST client
2. Writes data to SAP HANA Database

## Environment Variables

### Module Specific
The following module configurations can be provided in a data service designer section on weeve platform:

| Name                 | Environment Variables | type    | Description                                               |
| -------------------- | --------------------- | ------- | --------------------------------------------------------- |
| HDB Address          | HDB_ADDRESS           | string  | HANA DB schema address                                    |
| HDB Port             | HDB_PORT              | integer | HANA DB schema port                                       |
| HDB Schema Username  | HDB_USER              | string  | HANA DB schema username                                   |
| HDB Schema Password  | HDB_PASSWORD          | string  | HANA DB schema password                                   |
| HDB Schema Name      | HDB_SCHEMA            | string  | HANA DB schema holding the table                          |
| HDB Table Name       | HDB_TABLE             | string  | HANA DB table to write to                                 |
| HDB Column Headers   | HDB_HEADERS           | string  | List of comma (,) separated HANA DB table column headers. |
| Data Labels          | LABELS                | string  | List of comma (,) separated labels in passed data. Order of labels must match the order of provided corresponding headers. |

***

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

### Set by the weeve Agent on the edge-node

| Environment Variables | type   | Description                                       |
| --------------------- | ------ | ------------------------------------------------- |
| MODULE_NAME           | string | Name of the module                                |
| MODULE_TYPE           | string | Type of the module (ingress, processing, egress)  |
| EGRESS_SCHEME         | string | URL Scheme                                        |
| EGRESS_HOST           | string | URL target host                                   |
| EGRESS_PORT           | string | URL target port                                   |
| EGRESS_PATH           | string | URL target path                                   |
| EGRESS_URL            | string | HTTP ReST endpoint for the next module            |
| INGRESS_HOST          | string | URL local host                                    |
| INGRESS_PORT          | string | URL local port                                    |
| INGRESS_PATH          | string | URL local path                                    |

## Dependencies

```txt
Flask==1.1.1
requests
python-dotenv
hdbcli
```

## Examples

### Input

```json
// Single item
{
  "temperature": 10
}
// Batch of data
[
  {
  "temperature": 10.01
  },
  {
  "temperature": 12.23
  }
]
```

### Output

There is no output for this module, except data written to a database.

## docker-compose example

```yml
version: "3"
services:
  sap-hana-db-egress:
    image: weevenetwork/sap-hana-database-egress
    environment:
      MODULE_NAME: sap-hana-database-egress
      EGRESS_URL: None
      INGRESS_HOST: 0.0.0.0
      INGRESS_PORT: 80
      HDB_ADDRESS: f4a3724b752e.hana.us10.hanacloud.com
      HDB_PORT: 443
      HDB_USER: user
      HDB_PASSWORD: password
      HDB_SCHEMA: schema
      HDB_TABLE: table
      HDB_HEADERS: "temp, text, rand"
      LABELS: "temp, test, random"
    ports:
      - 5000:80
```
