---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - operational_insights
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
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.operational_insights.workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `eTag` | `string` | The ETag of the workspace. |
| `features` | `object` | Workspace features. |
| `forceCmkForQuery` | `boolean` | Indicates whether customer managed storage is mandatory for query management. |
| `retentionInDays` | `integer` | The workspace data retention in days. Allowed values are per pricing plan. See pricing tiers documentation for details. |
| `tags` | `object` | Resource tags. |
| `workspaceCapping` | `object` | The daily volume cap for ingestion. |
| `defaultDataCollectionRuleResourceId` | `string` | The resource ID of the default Data Collection Rule to use for this workspace. Expected format is - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/dataCollectionRules/{dcrName}. |
| `customerId` | `string` | This is a read-only property. Represents the ID associated with the workspace. |
| `provisioningState` | `string` | The provisioning state of the workspace. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `privateLinkScopedResources` | `array` | List of linked private link scope resources. |
| `publicNetworkAccessForQuery` | `string` | The network access type for operating on the Log Analytics Workspace. By default it is Enabled |
| `publicNetworkAccessForIngestion` | `string` | The network access type for operating on the Log Analytics Workspace. By default it is Enabled |
| `sku` | `object` | The SKU (tier) of a workspace. |
| `createdDate` | `string` | Workspace creation date. |
| `location` | `string` | The geo-location where the resource lives |
| `modifiedDate` | `string` | Workspace modification date. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Workspaces_List` | `SELECT` | `subscriptionId` | Gets the workspaces in a subscription. |
| `Workspaces_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets workspaces in a resource group. |
| `Workspaces_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, workspaceName` | Create or update a workspace. |
| `Workspaces_Delete` | `DELETE` | `resourceGroupName, subscriptionId, workspaceName` | Deletes a workspace resource. To recover the workspace, create it again with the same name, in the same subscription, resource group and location. The name is kept for 14 days and cannot be used for another workspace. To remove the workspace completely and release the name, use the force flag. |
| `Workspaces_Get` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Gets a workspace instance. |
| `Workspaces_Update` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Updates a workspace. |
