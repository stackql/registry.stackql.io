---
title: virtual_wans
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_wans
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
<tr><td><b>Name</b></td><td><code>virtual_wans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_wans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `disableVpnEncryption` | `boolean` | Vpn encryption to be disabled or not. |
| `type` | `string` | Resource type. |
| `vpnSites` | `array` | List of VpnSites in the VirtualWAN. |
| `office365LocalBreakoutCategory` | `string` | The office traffic category. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | Resource location. |
| `allowVnetToVnetTraffic` | `boolean` | True if Vnet to Vnet traffic is allowed. |
| `virtualHubs` | `array` | List of VirtualHubs in the VirtualWAN. |
| `provisioningState` | `string` | The current provisioning state. |
| `allowBranchToBranchTraffic` | `boolean` | True if branch to branch traffic is allowed. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualWans_List` | `SELECT` | `subscriptionId` | Lists all the VirtualWANs in a subscription. |
| `VirtualWans_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the VirtualWANs in a resource group. |
| `VirtualWans_CreateOrUpdate` | `INSERT` | `VirtualWANName, resourceGroupName, subscriptionId, data__location` | Creates a VirtualWAN resource if it doesn't exist else updates the existing VirtualWAN. |
| `VirtualWans_Delete` | `DELETE` | `VirtualWANName, resourceGroupName, subscriptionId` | Deletes a VirtualWAN. |
| `VirtualWans_Get` | `EXEC` | `VirtualWANName, resourceGroupName, subscriptionId` | Retrieves the details of a VirtualWAN. |
| `VirtualWans_UpdateTags` | `EXEC` | `VirtualWANName, resourceGroupName, subscriptionId` | Updates a VirtualWAN tags. |