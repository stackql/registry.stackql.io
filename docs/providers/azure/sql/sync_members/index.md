---
title: sync_members
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_members
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
<tr><td><b>Name</b></td><td><code>sync_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.sync_members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `sqlServerDatabaseId` | `string` | SQL Server database id of the sync member. |
| `userName` | `string` | User name of the member database in the sync member. |
| `password` | `string` | Password of the member database in the sync member. |
| `privateEndpointName` | `string` | Private endpoint name of the sync member if use private link connection is enabled, for sync members in Azure. |
| `serverName` | `string` | Server name of the member database in the sync member |
| `syncAgentId` | `string` | ARM resource id of the sync agent in the sync member. |
| `databaseType` | `string` | Database type of the sync member. |
| `syncDirection` | `string` | Sync direction of the sync member. |
| `syncMemberAzureDatabaseResourceId` | `string` | ARM resource id of the sync member logical database, for sync members in Azure. |
| `usePrivateLinkConnection` | `boolean` | Whether to use private link connection. |
| `databaseName` | `string` | Database name of the member database in the sync member. |
| `syncState` | `string` | Sync state of the sync member. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SyncMembers_ListBySyncGroup` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Lists sync members in the given sync group. |
| `SyncMembers_CreateOrUpdate` | `INSERT` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName` | Creates or updates a sync member. |
| `SyncMembers_Delete` | `DELETE` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName` | Deletes a sync member. |
| `SyncMembers_Get` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName` | Gets a sync member. |
| `SyncMembers_ListMemberSchemas` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName` | Gets a sync member database schema. |
| `SyncMembers_RefreshMemberSchema` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName` | Refreshes a sync member database schema. |
| `SyncMembers_Update` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName` | Updates an existing sync member. |
