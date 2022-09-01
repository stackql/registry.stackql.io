---
title: bookmarks
hide_title: false
hide_table_of_contents: false
keywords:
  - bookmarks
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
<tr><td><b>Name</b></td><td><code>bookmarks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.bookmarks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `incidentInfo` | `object` | Describes related incident information for the bookmark |
| `displayName` | `string` | The display name of the bookmark |
| `createdBy` | `object` | User information that made some action |
| `labels` | `array` | List of labels relevant to this bookmark |
| `updated` | `string` | The last time the bookmark was updated |
| `etag` | `string` | Etag of the azure resource |
| `queryEndTime` | `string` | The end time for the query |
| `created` | `string` | The time the bookmark was created |
| `notes` | `string` | The notes of the bookmark |
| `updatedBy` | `object` | User information that made some action |
| `queryStartTime` | `string` | The start time for the query |
| `tactics` | `array` | A list of relevant mitre attacks |
| `entityMappings` | `array` | Describes the entity mappings of the bookmark |
| `eventTime` | `string` | The bookmark event time |
| `query` | `string` | The query of the bookmark. |
| `queryResult` | `string` | The query result of the bookmark. |
| `techniques` | `array` | A list of relevant mitre techniques |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Bookmarks_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all bookmarks. |
| `Bookmarks_CreateOrUpdate` | `INSERT` | `bookmarkId, resourceGroupName, subscriptionId, workspaceName` | Creates or updates the bookmark. |
| `Bookmarks_Delete` | `DELETE` | `bookmarkId, resourceGroupName, subscriptionId, workspaceName` | Delete the bookmark. |
| `Bookmarks_Get` | `EXEC` | `bookmarkId, resourceGroupName, subscriptionId, workspaceName` | Gets a bookmark. |
