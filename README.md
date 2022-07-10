# SAP HANA Database Egress

|                |                                       |
| -------------- | ------------------------------------- |
| Name           | SAP HANA Database Egress              |
| Version        | v1.0.0                                |
| DockerHub      | [weevenetwork/sap-hana-database-egress](https://hub.docker.com/r/weevenetwork/sap-hana-database-egress) |
| authors        | Jakub Grzelak                    |

- [SAP HANA Database Egress](#sap-hana-database-egress)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

This module allows to save data in a selected SAP HANA Database Scheme and Table. Currently this module supports only AMD architecture.

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


### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)  |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle
requests
hdbcli
```

## Input

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

## Output

There is no output for this module, except data written to a database.

