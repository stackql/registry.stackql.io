---
title: virtual_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks
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
<tr><td><b>Name</b></td><td><code>virtual_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `provisioningState` | `string` | The current provisioning state. |
| `tags` | `object` | Resource tags. |
| `addressSpace` | `object` | AddressSpace contains an array of IP address ranges that can be used by subnets of the virtual network. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `bgpCommunities` | `object` | Bgp Communities sent over ExpressRoute with each route corresponding to a prefix in this VNET. |
| `location` | `string` | Resource location. |
| `virtualNetworkPeerings` | `array` | A list of peerings in a Virtual Network. |
| `type` | `string` | Resource type. |
| `resourceGuid` | `string` | The resourceGuid property of the Virtual Network resource. |
| `enableDdosProtection` | `boolean` | Indicates if DDoS protection is enabled for all the protected resources in the virtual network. It requires a DDoS protection plan associated with the resource. |
| `encryption` | `object` | Indicates if encryption is enabled on virtual network and if VM without encryption is allowed in encrypted VNet. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `subnets` | `array` | A list of subnets in a Virtual Network. |
| `ipAllocations` | `array` | Array of IpAllocation which reference this VNET. |
| `dhcpOptions` | `object` | DhcpOptions contains an array of DNS servers available to VMs deployed in the virtual network. Standard DHCP option for a subnet overrides VNET DHCP options. |
| `flowTimeoutInMinutes` | `integer` | The FlowTimeout value (in minutes) for the Virtual Network |
| `ddosProtectionPlan` | `object` | Reference to another subresource. |
| `enableVmProtection` | `boolean` | Indicates if VM protection is enabled for all the subnets in the virtual network. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualNetworks_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all virtual networks in a resource group. |
| `VirtualNetworks_ListAll` | `SELECT` | `subscriptionId` | Gets all virtual networks in a subscription. |
| `VirtualNetworks_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, virtualNetworkName` | Creates or updates a virtual network in the specified resource group. |
| `VirtualNetworks_Delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualNetworkName` | Deletes the specified virtual network. |
| `VirtualNetworks_CheckIPAddressAvailability` | `EXEC` | `ipAddress, resourceGroupName, subscriptionId, virtualNetworkName` | Checks whether a private IP address is available for use. |
| `VirtualNetworks_Get` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkName` | Gets the specified virtual network by resource group. |
| `VirtualNetworks_ListUsage` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkName` | Lists usage stats. |
| `VirtualNetworks_UpdateTags` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkName` | Updates a virtual network tags. |
