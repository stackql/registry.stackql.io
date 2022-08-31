---
title: express_route_circuit_peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_circuit_peerings
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
<tr><td><b>Name</b></td><td><code>express_route_circuit_peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.express_route_circuit_peerings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `expressRouteConnection` | `object` | The ID of the ExpressRouteConnection. |
| `secondaryAzurePort` | `string` | The secondary port. |
| `peeredConnections` | `array` | The list of peered circuit connections associated with Azure Private Peering for this circuit. |
| `peeringType` | `string` | The peering type. |
| `ipv6PeeringConfig` | `object` | Contains IPv6 peering config. |
| `microsoftPeeringConfig` | `object` | Specifies the peering configuration. |
| `routeFilter` | `object` | Reference to another subresource. |
| `connections` | `array` | The list of circuit connections associated with Azure Private Peering for this circuit. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `gatewayManagerEtag` | `string` | The GatewayManager Etag. |
| `primaryPeerAddressPrefix` | `string` | The primary address prefix. |
| `azureASN` | `integer` | The Azure ASN. |
| `sharedKey` | `string` | The shared key. |
| `provisioningState` | `string` | The current provisioning state. |
| `vlanId` | `integer` | The VLAN ID. |
| `stats` | `object` | Contains stats associated with the peering. |
| `state` | `string` | The state of peering. |
| `type` | `string` | Type of the resource. |
| `secondaryPeerAddressPrefix` | `string` | The secondary address prefix. |
| `lastModifiedBy` | `string` | Who was the last to modify the peering. |
| `primaryAzurePort` | `string` | The primary port. |
| `peerASN` | `integer` | The peer ASN. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ExpressRouteCircuitPeerings_List` | `SELECT` | `circuitName, resourceGroupName, subscriptionId` | Gets all peerings in a specified express route circuit. |
| `ExpressRouteCircuitPeerings_CreateOrUpdate` | `INSERT` | `circuitName, peeringName, resourceGroupName, subscriptionId` | Creates or updates a peering in the specified express route circuits. |
| `ExpressRouteCircuitPeerings_Delete` | `DELETE` | `circuitName, peeringName, resourceGroupName, subscriptionId` | Deletes the specified peering from the specified express route circuit. |
| `ExpressRouteCircuitPeerings_Get` | `EXEC` | `circuitName, peeringName, resourceGroupName, subscriptionId` | Gets the specified peering for the express route circuit. |