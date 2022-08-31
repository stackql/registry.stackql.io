---
title: managed_database_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_queries
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
<tr><td><b>Name</b></td><td><code>managed_database_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_database_queries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `queryId` | `string` | Unique query id (unique within one database). |
| `startTime` | `string` | The start time for the metric (ISO-8601 format). |
| `databaseName` | `string` | Database name of the database in which this query was executed. |
| `endTime` | `string` | The end time for the metric (ISO-8601 format). |
| `intervals` | `array` | List of intervals with appropriate metric data |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedDatabaseQueries_ListByQuery` | `SELECT` | `databaseName, managedInstanceName, queryId, resourceGroupName, subscriptionId` | Get query execution statistics by query id. |
| `ManagedDatabaseQueries_Get` | `EXEC` | `databaseName, managedInstanceName, queryId, resourceGroupName, subscriptionId` | Get query by query id. |
