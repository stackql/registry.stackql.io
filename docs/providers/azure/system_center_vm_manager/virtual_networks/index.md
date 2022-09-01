---
title: virtual_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks
  - system_center_vm_manager
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
<tr><td><b>Name</b></td><td><code>virtual_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.system_center_vm_manager.virtual_networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `tags` | `object` | Resource tags |
| `inventoryItemId` | `string` | Gets or sets the inventory Item ID for the resource. |
| `networkName` | `string` | Name of the virtual network in vmmServer. |
| `provisioningState` | `string` | Gets or sets the provisioning state. |
| `location` | `string` | Gets or sets the location. |
| `type` | `string` | Resource Type |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `extendedLocation` | `object` | The extended location. |
| `uuid` | `string` | Unique ID of the virtual network. |
| `vmmServerId` | `string` | ARM Id of the vmmServer resource in which this resource resides. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualNetworks_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List of VirtualNetworks in a resource group. |
| `VirtualNetworks_ListBySubscription` | `SELECT` | `subscriptionId` | List of VirtualNetworks in a subscription. |
| `VirtualNetworks_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, virtualNetworkName, data__extendedLocation, data__location` | Onboards the ScVmm virtual network as an Azure virtual network resource. |
| `VirtualNetworks_Delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualNetworkName` | Deregisters the ScVmm virtual network from Azure. |
| `VirtualNetworks_Get` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkName` | Implements VirtualNetwork GET method. |
| `VirtualNetworks_Update` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkName` | Updates the VirtualNetworks resource. |
