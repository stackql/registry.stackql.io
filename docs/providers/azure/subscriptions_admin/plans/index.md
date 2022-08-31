---
title: plans
hide_title: false
hide_table_of_contents: false
keywords:
  - plans
  - subscriptions_admin
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
<tr><td><b>Name</b></td><td><code>plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.subscriptions_admin.plans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `description` | `string` | Description of the plan. |
| `displayName` | `string` | Display name. |
| `skuIds` | `array` | SKU identifiers. |
| `externalReferenceId` | `string` | External reference identifier. |
| `type` | `string` | Type of resource. |
| `subscriptionCount` | `integer` | Subscription count. |
| `quotaIds` | `array` | Quota identifiers under the plan. |
| `tags` | `object` | List of key-value pairs. |
| `location` | `string` | Location of the resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Plans_List` | `SELECT` | `resourceGroupName, subscriptionId` | Get the list of plans under a resource group. |
| `Plans_ListAll` | `SELECT` | `subscriptionId` | List all plans across all subscriptions. |
| `Plans_CreateOrUpdate` | `INSERT` | `plan, resourceGroupName, subscriptionId` | Create or update the plan. |
| `Plans_Delete` | `DELETE` | `plan, resourceGroupName, subscriptionId` | Delete the specified plan. |
| `Plans_Get` | `EXEC` | `plan, resourceGroupName, subscriptionId` | Get the specified plan. |
| `Plans_ListMetricDefinitions` | `EXEC` | `plan, resourceGroupName, subscriptionId` | Get the metric definitions of the specified plan. |
| `Plans_ListMetrics` | `EXEC` | `plan, resourceGroupName, subscriptionId` | Get the metrics of the specified plan. |
