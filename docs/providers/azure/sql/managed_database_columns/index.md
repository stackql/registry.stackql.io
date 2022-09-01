---
title: managed_database_columns
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_columns
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
<tr><td><b>Name</b></td><td><code>managed_database_columns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_database_columns</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `columnType` | `string` | The column data type. |
| `isComputed` | `boolean` | Whether or not the column is computed. |
| `memoryOptimized` | `boolean` | Whether or not the column belongs to a memory optimized table. |
| `temporalType` | `string` | The table temporal type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedDatabaseColumns_ListByDatabase` | `SELECT` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` | List managed database columns |
| `ManagedDatabaseColumns_ListByTable` | `SELECT` | `databaseName, managedInstanceName, resourceGroupName, schemaName, subscriptionId, tableName` | List managed database columns |
| `ManagedDatabaseColumns_Get` | `EXEC` | `columnName, databaseName, managedInstanceName, resourceGroupName, schemaName, subscriptionId, tableName` | Get managed database column |
