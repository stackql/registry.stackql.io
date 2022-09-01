---
title: management_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - management_groups
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
<tr><td><b>Name</b></td><td><code>management_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.operational_insights.management_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique ID of the management group. |
| `name` | `string` | The name of the management group. |
| `serverCount` | `integer` | The number of servers connected to the management group. |
| `sku` | `string` | The SKU of System Center that is managing the management group. |
| `version` | `string` | The version of System Center that is managing the management group. |
| `created` | `string` | The datetime that the management group was created. |
| `dataReceived` | `string` | The last datetime that the management group received data. |
| `isGateway` | `boolean` | Gets or sets a value indicating whether the management group is a gateway. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ManagementGroups_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
