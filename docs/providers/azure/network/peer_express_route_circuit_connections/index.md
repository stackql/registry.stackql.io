---
title: peer_express_route_circuit_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - peer_express_route_circuit_connections
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
<tr><td><b>Name</b></td><td><code>peer_express_route_circuit_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.peer_express_route_circuit_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `provisioningState` | `string` | The current provisioning state. |
| `expressRouteCircuitPeering` | `object` | Reference to another subresource. |
| `connectionName` | `string` | The name of the express route circuit connection resource. |
| `addressPrefix` | `string` | /29 IP address space to carve out Customer addresses for tunnels. |
| `authResourceGuid` | `string` | The resource guid of the authorization used for the express route circuit connection. |
| `peerExpressRouteCircuitPeering` | `object` | Reference to another subresource. |
| `circuitConnectionStatus` | `string` | Express Route Circuit connection state. |
| `type` | `string` | Type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PeerExpressRouteCircuitConnections_List` | `SELECT` | `circuitName, peeringName, resourceGroupName, subscriptionId` | Gets all global reach peer connections associated with a private peering in an express route circuit. |
| `PeerExpressRouteCircuitConnections_Get` | `EXEC` | `circuitName, connectionName, peeringName, resourceGroupName, subscriptionId` | Gets the specified Peer Express Route Circuit Connection from the specified express route circuit. |
