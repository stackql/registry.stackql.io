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
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `publicNetworkAccessForQuery` | `string` | The network access type for operating on the Log Analytics Workspace. By default it is Enabled |
| `retentionInDays` | `integer` | The workspace data retention in days. Allowed values are per pricing plan. See pricing tiers documentation for details. |
| `tags` | `object` | Resource tags. |
| `provisioningState` | `string` | The provisioning state of the workspace. |
| `publicNetworkAccessForIngestion` | `string` | The network access type for operating on the Log Analytics Workspace. By default it is Enabled |
| `defaultDataCollectionRuleResourceId` | `string` | The resource ID of the default Data Collection Rule to use for this workspace. Expected format is - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Insights/dataCollectionRules/&#123;dcrName&#125;. |
| `eTag` | `string` | The ETag of the workspace. |
| `forceCmkForQuery` | `boolean` | Indicates whether customer managed storage is mandatory for query management. |
| `workspaceCapping` | `object` | The daily volume cap for ingestion. |
| `createdDate` | `string` | Workspace creation date. |
| `features` | `object` | Workspace features. |
| `modifiedDate` | `string` | Workspace modification date. |
| `privateLinkScopedResources` | `array` | List of linked private link scope resources. |
| `customerId` | `string` | This is a read-only property. Represents the ID associated with the workspace. |
| `sku` | `object` | The SKU (tier) of a workspace. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DeletedWorkspaces_List` | `SELECT` | `subscriptionId` | Gets recently deleted workspaces in a subscription, available for recovery. |
| `DeletedWorkspaces_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets recently deleted workspaces in a resource group, available for recovery. |
