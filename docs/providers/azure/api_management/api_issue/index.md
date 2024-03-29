---
title: api_issue
hide_title: false
hide_table_of_contents: false
keywords:
  - api_issue
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
<tr><td><b>Name</b></td><td><code>api_issue</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api_issue</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Issue contract Properties. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApiIssue_Get` | `SELECT` | `apiId, issueId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the Issue for an API specified by its identifier. |
| `ApiIssue_ListByService` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId` | Lists all issues associated with the specified API. |
| `ApiIssue_CreateOrUpdate` | `INSERT` | `apiId, issueId, resourceGroupName, serviceName, subscriptionId` | Creates a new Issue for an API or updates an existing one. |
| `ApiIssue_Delete` | `DELETE` | `If-Match, apiId, issueId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified Issue from an API. |
| `ApiIssue_GetEntityTag` | `EXEC` | `apiId, issueId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the Issue for an API specified by its identifier. |
| `ApiIssue_Update` | `EXEC` | `If-Match, apiId, issueId, resourceGroupName, serviceName, subscriptionId` | Updates an existing issue for an API. |
