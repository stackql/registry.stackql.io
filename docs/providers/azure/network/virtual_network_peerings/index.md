---
title: virtual_network_peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_peerings
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
<tr><td><b>Name</b></td><td><code>virtual_network_peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_network_peerings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `remoteVirtualNetworkEncryption` | `object` | Indicates if encryption is enabled on virtual network and if VM without encryption is allowed in encrypted VNet. |
| `useRemoteGateways` | `boolean` | If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, virtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway. |
| `peeringSyncLevel` | `string` | The peering sync status of the virtual network peering. |
| `remoteBgpCommunities` | `object` | Bgp Communities sent over ExpressRoute with each route corresponding to a prefix in this VNET. |
| `remoteVirtualNetwork` | `object` | Reference to another subresource. |
| `provisioningState` | `string` | The current provisioning state. |
| `peeringState` | `string` | The status of the virtual network peering. |
| `remoteAddressSpace` | `object` | AddressSpace contains an array of IP address ranges that can be used by subnets of the virtual network. |
| `allowForwardedTraffic` | `boolean` | Whether the forwarded traffic from the VMs in the local virtual network will be allowed/disallowed in remote virtual network. |
| `doNotVerifyRemoteGateways` | `boolean` | If we need to verify the provisioning state of the remote gateway. |
| `resourceGuid` | `string` | The resourceGuid property of the Virtual Network peering resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `allowVirtualNetworkAccess` | `boolean` | Whether the VMs in the local virtual network space would be able to access the VMs in remote virtual network space. |
| `allowGatewayTransit` | `boolean` | If gateway links can be used in remote virtual networking to link to this virtual network. |
| `type` | `string` | Resource type. |
| `remoteVirtualNetworkAddressSpace` | `object` | AddressSpace contains an array of IP address ranges that can be used by subnets of the virtual network. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualNetworkPeerings_List` | `SELECT` | `resourceGroupName, subscriptionId, virtualNetworkName` | Gets all virtual network peerings in a virtual network. |
| `VirtualNetworkPeerings_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, virtualNetworkName, virtualNetworkPeeringName` | Creates or updates a peering in the specified virtual network. |
| `VirtualNetworkPeerings_Delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualNetworkName, virtualNetworkPeeringName` | Deletes the specified virtual network peering. |
| `VirtualNetworkPeerings_Get` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkName, virtualNetworkPeeringName` | Gets the specified virtual network peering. |
