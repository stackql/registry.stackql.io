---
title: api_issue_comment
hide_title: false
hide_table_of_contents: false
keywords:
  - api_issue_comment
  - api_management
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
<tr><td><b>Name</b></td><td><code>api_issue_comment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api_issue_comment</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `userId` | `string` | A resource identifier for the user who left the comment. |
| `createdDate` | `string` | Date and time when the comment was created. |
| `text` | `string` | Comment text. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApiIssueComment_ListByService` | `SELECT` | `apiId, issueId, resourceGroupName, serviceName, subscriptionId` | Lists all comments for the Issue associated with the specified API. |
| `ApiIssueComment_CreateOrUpdate` | `INSERT` | `apiId, commentId, issueId, resourceGroupName, serviceName, subscriptionId` | Creates a new Comment for the Issue in an API or updates an existing one. |
| `ApiIssueComment_Delete` | `DELETE` | `If-Match, apiId, commentId, issueId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified comment from an Issue. |
| `ApiIssueComment_Get` | `EXEC` | `apiId, commentId, issueId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the issue Comment for an API specified by its identifier. |
| `ApiIssueComment_GetEntityTag` | `EXEC` | `apiId, commentId, issueId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the issue Comment for an API specified by its identifier. |
