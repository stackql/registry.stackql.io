---
title: bookmark_relations
hide_title: false
hide_table_of_contents: false
keywords:
  - bookmark_relations
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
<tr><td><b>Name</b></td><td><code>bookmark_relations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.bookmark_relations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `relatedResourceId` | `string` | The resource ID of the related resource |
| `relatedResourceKind` | `string` | The resource kind of the related resource |
| `relatedResourceName` | `string` | The name of the related resource |
| `relatedResourceType` | `string` | The resource type of the related resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BookmarkRelations_List` | `SELECT` | `bookmarkId, resourceGroupName, subscriptionId, workspaceName` | Gets all bookmark relations. |
| `BookmarkRelations_CreateOrUpdate` | `INSERT` | `bookmarkId, relationName, resourceGroupName, subscriptionId, workspaceName` | Creates the bookmark relation. |
| `BookmarkRelations_Delete` | `DELETE` | `bookmarkId, relationName, resourceGroupName, subscriptionId, workspaceName` | Delete the bookmark relation. |
| `BookmarkRelations_Get` | `EXEC` | `bookmarkId, relationName, resourceGroupName, subscriptionId, workspaceName` | Gets a bookmark relation. |
