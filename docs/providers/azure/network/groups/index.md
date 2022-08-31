---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - network
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
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `description` | `string` | A description of the network group. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `provisioningState` | `string` | The current provisioning state. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NetworkGroups_List` | `SELECT` | `networkManagerName, resourceGroupName, subscriptionId` | Lists the specified network group. |
| `NetworkGroups_CreateOrUpdate` | `INSERT` |  | Creates or updates a network group. |
| `NetworkGroups_Delete` | `DELETE` |  | Deletes a network group. |
| `NetworkGroups_Get` | `EXEC` |  | Gets the specified network group. |
