---
title: vnet_peering
hide_title: false
hide_table_of_contents: false
keywords:
  - vnet_peering
  - databricks
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
<tr><td><b>Name</b></td><td><code>vnet_peering</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.databricks.vnet_peering</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Name of the virtual network peering resource |
| `type` | `string` | type of the virtual network peering resource |
| `databricksVirtualNetwork` | `` |  The remote virtual network should be in the same region. See here to learn more (https://docs.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-peering). |
| `peeringState` | `string` | The status of the virtual network peering. |
| `remoteVirtualNetwork` | `` |  The remote virtual network should be in the same region. See here to learn more (https://docs.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-peering). |
| `allowForwardedTraffic` | `boolean` | Whether the forwarded traffic from the VMs in the local virtual network will be allowed/disallowed in remote virtual network. |
| `allowGatewayTransit` | `boolean` | If gateway links can be used in remote virtual networking to link to this virtual network. |
| `remoteAddressSpace` | `object` | AddressSpace contains an array of IP address ranges that can be used by subnets of the virtual network. |
| `allowVirtualNetworkAccess` | `boolean` | Whether the VMs in the local virtual network space would be able to access the VMs in remote virtual network space. |
| `provisioningState` | `string` | The current provisioning state. |
| `databricksAddressSpace` | `object` | AddressSpace contains an array of IP address ranges that can be used by subnets of the virtual network. |
| `useRemoteGateways` | `boolean` | If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, virtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `vNetPeering_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Lists the workspace vNet Peerings. |
| `vNetPeering_CreateOrUpdate` | `INSERT` | `peeringName, resourceGroupName, subscriptionId, workspaceName` | Creates vNet Peering for workspace. |
| `vNetPeering_Delete` | `DELETE` | `peeringName, resourceGroupName, subscriptionId, workspaceName` | Deletes the workspace vNetPeering. |
| `vNetPeering_Get` | `EXEC` | `peeringName, resourceGroupName, subscriptionId, workspaceName` | Gets the workspace vNet Peering. |
