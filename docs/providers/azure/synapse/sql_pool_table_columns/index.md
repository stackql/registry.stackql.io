---
title: sql_pool_table_columns
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_table_columns
  - synapse
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
<tr><td><b>Name</b></td><td><code>sql_pool_table_columns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.sql_pool_table_columns</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `columnType` | `string` | The column data type. |
| `isComputed` | `boolean` | Indicates whether column value is computed or not |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `SqlPoolTableColumns_ListByTableName` | `SELECT` | `resourceGroupName, schemaName, sqlPoolName, subscriptionId, tableName, workspaceName` |