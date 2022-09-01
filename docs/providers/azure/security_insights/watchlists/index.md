---
title: watchlists
hide_title: false
hide_table_of_contents: false
keywords:
  - watchlists
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
<tr><td><b>Name</b></td><td><code>watchlists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.watchlists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | A description of the watchlist |
| `tenantId` | `string` | The tenantId where the watchlist belongs to |
| `defaultDuration` | `string` | The default duration of a watchlist (in ISO 8601 duration format) |
| `createdBy` | `object` | User information that made some action |
| `uploadStatus` | `string` | The status of the Watchlist upload : New, InProgress or Complete. Pls note : When a Watchlist upload status is equal to InProgress, the Watchlist cannot be deleted |
| `source` | `string` | The filename of the watchlist, called 'source' |
| `displayName` | `string` | The display name of the watchlist |
| `created` | `string` | The time the watchlist was created |
| `contentType` | `string` | The content type of the raw content. Example : text/csv or text/tsv  |
| `updated` | `string` | The last time the watchlist was updated |
| `rawContent` | `string` | The raw content that represents to watchlist items to create. In case of csv/tsv content type, it's the content of the file that will parsed by the endpoint |
| `numberOfLinesToSkip` | `integer` | The number of lines in a csv/tsv content to skip before the header |
| `watchlistType` | `string` | The type of the watchlist |
| `sourceType` | `string` | The sourceType of the watchlist |
| `updatedBy` | `object` | User information that made some action |
| `etag` | `string` | Etag of the azure resource |
| `watchlistId` | `string` | The id (a Guid) of the watchlist |
| `itemsSearchKey` | `string` | The search key is used to optimize query performance when using watchlists for joins with other data. For example, enable a column with IP addresses to be the designated SearchKey field, then use this field as the key field when joining to other event data by IP address. |
| `watchlistAlias` | `string` | The alias of the watchlist |
| `provider` | `string` | The provider of the watchlist |
| `labels` | `array` | List of labels relevant to this watchlist |
| `isDeleted` | `boolean` | A flag that indicates if the watchlist is deleted or not |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Watchlists_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all watchlists, without watchlist items. |
| `Watchlists_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, watchlistAlias, workspaceName` | Create or update a Watchlist and its Watchlist Items (bulk creation, e.g. through text/csv content type). To create a Watchlist and its Items, we should call this endpoint with either rawContent or a valid SAR URI and contentType properties. The rawContent is mainly used for small watchlist (content size below 3.8 MB). The SAS URI enables the creation of large watchlist, where the content size can go up to 500 MB. The status of processing such large file can be polled through the URL returned in Azure-AsyncOperation header. |
| `Watchlists_Delete` | `DELETE` | `resourceGroupName, subscriptionId, watchlistAlias, workspaceName` | Delete a watchlist. |
| `Watchlists_Get` | `EXEC` | `resourceGroupName, subscriptionId, watchlistAlias, workspaceName` | Gets a watchlist, without its watchlist items. |
