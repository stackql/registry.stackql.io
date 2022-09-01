---
title: sync_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_groups
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
<tr><td><b>Name</b></td><td><code>sync_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.sync_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `schema` | `object` | Properties of sync group schema. |
| `syncDatabaseId` | `string` | ARM resource id of the sync database in the sync group. |
| `enableConflictLogging` | `boolean` | If conflict logging is enabled. |
| `conflictResolutionPolicy` | `string` | Conflict resolution policy of the sync group. |
| `hubDatabasePassword` | `string` | Password for the sync group hub database credential. |
| `hubDatabaseUserName` | `string` | User name for the sync group hub database credential. |
| `lastSyncTime` | `string` | Last sync time of the sync group. |
| `privateEndpointName` | `string` | Private endpoint name of the sync group if use private link connection is enabled. |
| `usePrivateLinkConnection` | `boolean` | If use private link connection is enabled. |
| `interval` | `integer` | Sync interval of the sync group. |
| `sku` | `object` | An ARM Resource SKU. |
| `syncState` | `string` | Sync state of the sync group. |
| `conflictLoggingRetentionInDays` | `integer` | Conflict logging retention period. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SyncGroups_ListByDatabase` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Lists sync groups under a hub database. |
| `SyncGroups_CreateOrUpdate` | `INSERT` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Creates or updates a sync group. |
| `SyncGroups_Delete` | `DELETE` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Deletes a sync group. |
| `SyncGroups_CancelSync` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Cancels a sync group synchronization. |
| `SyncGroups_Get` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Gets a sync group. |
| `SyncGroups_ListHubSchemas` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Gets a collection of hub database schemas. |
| `SyncGroups_ListLogs` | `EXEC` | `databaseName, endTime, resourceGroupName, serverName, startTime, subscriptionId, syncGroupName, type` | Gets a collection of sync group logs. |
| `SyncGroups_ListSyncDatabaseIds` | `EXEC` | `locationName, subscriptionId` | Gets a collection of sync database ids. |
| `SyncGroups_RefreshHubSchema` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Refreshes a hub database schema. |
| `SyncGroups_TriggerSync` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Triggers a sync group synchronization. |
| `SyncGroups_Update` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Updates a sync group. |
