---
title: elastic_pool_database_activities
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_pool_database_activities
  - sql
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>elastic_pool_database_activities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.elastic_pool_database_activities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `serverName` | `string` | The name of the server the elastic pool is in. |
| `location` | `string` | The geo-location where the resource lives |
| `state` | `string` | The current state of the operation. |
| `operationId` | `string` | The unique operation ID. |
| `currentElasticPoolName` | `string` | The name of the current elastic pool the database is in if available. |
| `endTime` | `string` | The time the operation finished (ISO8601 format). |
| `errorMessage` | `string` | The error message if available. |
| `requestedElasticPoolName` | `string` | The name for the elastic pool the database is moving into if available. |
| `databaseName` | `string` | The database name. |
| `errorCode` | `integer` | The error code if available. |
| `currentServiceObjective` | `string` | The name of the current service objective if available. |
| `percentComplete` | `integer` | The percentage complete if available. |
| `startTime` | `string` | The time the operation started (ISO8601 format). |
| `requestedServiceObjective` | `string` | The name of the requested service objective if available. |
| `errorSeverity` | `integer` | The error severity if available. |
| `operation` | `string` | The operation name. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ElasticPoolDatabaseActivities_ListByElasticPool` | `SELECT` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` |
