---
title: express_route_cross_connection_peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_cross_connection_peerings
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
<tr><td><b>Name</b></td><td><code>express_route_cross_connection_peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.express_route_cross_connection_peerings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `gatewayManagerEtag` | `string` | The GatewayManager Etag. |
| `microsoftPeeringConfig` | `object` | Specifies the peering configuration. |
| `sharedKey` | `string` | The shared key. |
| `peerASN` | `integer` | The peer ASN. |
| `secondaryAzurePort` | `string` | The secondary port. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `peeringType` | `string` | The peering type. |
| `primaryPeerAddressPrefix` | `string` | The primary address prefix. |
| `ipv6PeeringConfig` | `object` | Contains IPv6 peering config. |
| `state` | `string` | The state of peering. |
| `secondaryPeerAddressPrefix` | `string` | The secondary address prefix. |
| `vlanId` | `integer` | The VLAN ID. |
| `lastModifiedBy` | `string` | Who was the last to modify the peering. |
| `provisioningState` | `string` | The current provisioning state. |
| `azureASN` | `integer` | The Azure ASN. |
| `primaryAzurePort` | `string` | The primary port. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ExpressRouteCrossConnectionPeerings_List` | `SELECT` | `crossConnectionName, resourceGroupName, subscriptionId` | Gets all peerings in a specified ExpressRouteCrossConnection. |
| `ExpressRouteCrossConnectionPeerings_CreateOrUpdate` | `INSERT` | `crossConnectionName, peeringName, resourceGroupName, subscriptionId` | Creates or updates a peering in the specified ExpressRouteCrossConnection. |
| `ExpressRouteCrossConnectionPeerings_Delete` | `DELETE` | `crossConnectionName, peeringName, resourceGroupName, subscriptionId` | Deletes the specified peering from the ExpressRouteCrossConnection. |
| `ExpressRouteCrossConnectionPeerings_Get` | `EXEC` | `crossConnectionName, peeringName, resourceGroupName, subscriptionId` | Gets the specified peering for the ExpressRouteCrossConnection. |
