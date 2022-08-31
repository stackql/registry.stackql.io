---
title: deleted_workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_workspaces
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
<tr><td><b>Name</b></td><td><code>deleted_workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.operational_insights.deleted_workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `publicNetworkAccessForIngestion` | `string` | The network access type for operating on the Log Analytics Workspace. By default it is Enabled |
| `publicNetworkAccessForQuery` | `string` | The network access type for operating on the Log Analytics Workspace. By default it is Enabled |
| `defaultDataCollectionRuleResourceId` | `string` | The resource ID of the default Data Collection Rule to use for this workspace. Expected format is - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/dataCollectionRules/{dcrName}. |
| `features` | `object` | Workspace features. |
| `location` | `string` | The geo-location where the resource lives |
| `privateLinkScopedResources` | `array` | List of linked private link scope resources. |
| `workspaceCapping` | `object` | The daily volume cap for ingestion. |
| `tags` | `object` | Resource tags. |
| `customerId` | `string` | This is a read-only property. Represents the ID associated with the workspace. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `provisioningState` | `string` | The provisioning state of the workspace. |
| `sku` | `object` | The SKU (tier) of a workspace. |
| `modifiedDate` | `string` | Workspace modification date. |
| `retentionInDays` | `integer` | The workspace data retention in days. Allowed values are per pricing plan. See pricing tiers documentation for details. |
| `createdDate` | `string` | Workspace creation date. |
| `eTag` | `string` | The ETag of the workspace. |
| `forceCmkForQuery` | `boolean` | Indicates whether customer managed storage is mandatory for query management. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DeletedWorkspaces_List` | `SELECT` | `subscriptionId` | Gets recently deleted workspaces in a subscription, available for recovery. |
| `DeletedWorkspaces_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets recently deleted workspaces in a resource group, available for recovery. |
