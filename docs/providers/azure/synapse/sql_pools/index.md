---
title: sql_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pools
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
<tr><td><b>Name</b></td><td><code>sql_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.sql_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `maxSizeBytes` | `integer` | Maximum size in bytes |
| `location` | `string` | The geo-location where the resource lives |
| `storageAccountType` | `string` | The storage account type used to store backups for this sql pool. |
| `tags` | `object` | Resource tags. |
| `provisioningState` | `string` | Resource state |
| `restorePointInTime` | `string` | Snapshot time to restore |
| `sourceDatabaseId` | `string` | Source database to create from |
| `recoverableDatabaseId` | `string` | Backup database to restore from |
| `sourceDatabaseDeletionDate` | `string` | Specifies the time that the sql pool was deleted |
| `creationDate` | `string` | Date the SQL pool was created |
| `sku` | `object` | SQL pool SKU |
| `createMode` | `string` | Specifies the mode of sql pool creation.<br /><br />Default: regular sql pool creation.<br /><br />PointInTimeRestore: Creates a sql pool by restoring a point in time backup of an existing sql pool. sourceDatabaseId must be specified as the resource ID of the existing sql pool, and restorePointInTime must be specified.<br /><br />Recovery: Creates a sql pool by a geo-replicated backup. sourceDatabaseId  must be specified as the recoverableDatabaseId to restore.<br /><br />Restore: Creates a sql pool by restoring a backup of a deleted sql  pool. SourceDatabaseId should be the sql pool's original resource ID. SourceDatabaseId and sourceDatabaseDeletionDate must be specified. |
| `status` | `string` | Resource status |
| `collation` | `string` | Collation mode |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SqlPools_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | List all SQL pools |
| `SqlPools_Create` | `INSERT` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Create a SQL pool |
| `SqlPools_Delete` | `DELETE` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Delete a SQL pool |
| `SqlPools_Get` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get SQL pool properties |
| `SqlPools_Pause` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Pause a SQL pool |
| `SqlPools_Rename` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName, data__id` | Rename a SQL pool. |
| `SqlPools_Resume` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Resume a SQL pool |
| `SqlPools_Update` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Apply a partial update to a SQL pool |
