---
title: workspace_managed_sql_server_recoverable_sql_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_managed_sql_server_recoverable_sql_pools
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
<tr><td><b>Name</b></td><td><code>workspace_managed_sql_server_recoverable_sql_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.workspace_managed_sql_server_recoverable_sql_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `serviceLevelObjective` | `string` | The service level objective name of the database |
| `edition` | `string` | The edition of the database |
| `elasticPoolName` | `string` | The elastic pool name of the database |
| `lastAvailableBackupDate` | `string` | The last available backup date of the database (ISO8601 format) |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkspaceManagedSqlServerRecoverableSqlPools_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Get list of recoverable sql pools for workspace managed sql server. |
| `WorkspaceManagedSqlServerRecoverableSqlPools_Get` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get recoverable sql pools for workspace managed sql server. |
