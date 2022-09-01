---
title: watchlist_items
hide_title: false
hide_table_of_contents: false
keywords:
  - watchlist_items
  - security_insights
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
<tr><td><b>Name</b></td><td><code>watchlist_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.watchlist_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `createdBy` | `object` | User information that made some action |
| `updated` | `string` | The last time the watchlist item was updated |
| `updatedBy` | `object` | User information that made some action |
| `itemsKeyValue` | `object` | key-value pairs for a watchlist item |
| `watchlistItemId` | `string` | The id (a Guid) of the watchlist item |
| `entityMapping` | `object` | key-value pairs for a watchlist item entity mapping |
| `created` | `string` | The time the watchlist item was created |
| `isDeleted` | `boolean` | A flag that indicates if the watchlist item is deleted or not |
| `tenantId` | `string` | The tenantId to which the watchlist item belongs to |
| `etag` | `string` | Etag of the azure resource |
| `watchlistItemType` | `string` | The type of the watchlist item |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WatchlistItems_List` | `SELECT` | `resourceGroupName, subscriptionId, watchlistAlias, workspaceName` | Gets all watchlist Items. |
| `WatchlistItems_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, watchlistAlias, watchlistItemId, workspaceName` | Creates or updates a watchlist item. |
| `WatchlistItems_Delete` | `DELETE` | `resourceGroupName, subscriptionId, watchlistAlias, watchlistItemId, workspaceName` | Delete a watchlist item. |
| `WatchlistItems_Get` | `EXEC` | `resourceGroupName, subscriptionId, watchlistAlias, watchlistItemId, workspaceName` | Gets a watchlist, without its watchlist items. |
