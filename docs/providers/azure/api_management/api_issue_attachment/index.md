---
title: api_issue_attachment
hide_title: false
hide_table_of_contents: false
keywords:
  - api_issue_attachment
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
<tr><td><b>Name</b></td><td><code>api_issue_attachment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api_issue_attachment</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `content` | `string` | An HTTP link or Base64-encoded binary data. |
| `contentFormat` | `string` | Either 'link' if content is provided via an HTTP link or the MIME type of the Base64-encoded binary data provided in the 'content' property. |
| `title` | `string` | Filename by which the binary data will be saved. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApiIssueAttachment_ListByService` | `SELECT` | `apiId, issueId, resourceGroupName, serviceName, subscriptionId` | Lists all attachments for the Issue associated with the specified API. |
| `ApiIssueAttachment_CreateOrUpdate` | `INSERT` | `apiId, attachmentId, issueId, resourceGroupName, serviceName, subscriptionId` | Creates a new Attachment for the Issue in an API or updates an existing one. |
| `ApiIssueAttachment_Delete` | `DELETE` | `If-Match, apiId, attachmentId, issueId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified comment from an Issue. |
| `ApiIssueAttachment_Get` | `EXEC` | `apiId, attachmentId, issueId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the issue Attachment for an API specified by its identifier. |
| `ApiIssueAttachment_GetEntityTag` | `EXEC` | `apiId, attachmentId, issueId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the issue Attachment for an API specified by its identifier. |