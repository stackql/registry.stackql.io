---
title: virtual_network_gateway_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_gateway_connections
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
<tr><td><b>Name</b></td><td><code>virtual_network_gateway_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_network_gateway_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `routingWeight` | `integer` | The routing weight. |
| `tunnelConnectionStatus` | `array` | Collection of all tunnels' connection health status. |
| `type` | `string` | Resource type. |
| `provisioningState` | `string` | The current provisioning state. |
| `tags` | `object` | Resource tags. |
| `enableBgp` | `boolean` | EnableBgp flag. |
| `usePolicyBasedTrafficSelectors` | `boolean` | Enable policy-based traffic selectors. |
| `virtualNetworkGateway1` | `object` | A common class for general resource information. |
| `authorizationKey` | `string` | The authorizationKey. |
| `dpdTimeoutSeconds` | `integer` | The dead peer detection timeout of this connection in seconds. |
| `trafficSelectorPolicies` | `array` | The Traffic Selector Policies to be considered by this connection. |
| `location` | `string` | Resource location. |
| `gatewayCustomBgpIpAddresses` | `array` | GatewayCustomBgpIpAddresses to be used for virtual network gateway Connection. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `ipsecPolicies` | `array` | The IPSec Policies to be considered by this connection. |
| `connectionType` | `string` | Gateway connection type. |
| `ingressBytesTransferred` | `integer` | The ingress bytes transferred in this connection. |
| `localNetworkGateway2` | `object` | A common class for general resource information. |
| `connectionMode` | `string` | Gateway connection type. |
| `virtualNetworkGateway2` | `object` | A common class for general resource information. |
| `egressNatRules` | `array` | List of egress NatRules. |
| `egressBytesTransferred` | `integer` | The egress bytes transferred in this connection. |
| `expressRouteGatewayBypass` | `boolean` | Bypass ExpressRoute Gateway for data forwarding. |
| `sharedKey` | `string` | The IPSec shared key. |
| `connectionProtocol` | `string` | Gateway connection protocol. |
| `connectionStatus` | `string` | Virtual Network Gateway connection status. |
| `useLocalAzureIpAddress` | `boolean` | Use private local Azure IP for the connection. |
| `ingressNatRules` | `array` | List of ingress NatRules. |
| `peer` | `object` | Reference to another subresource. |
| `resourceGuid` | `string` | The resource GUID property of the virtual network gateway connection resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualNetworkGatewayConnections_List` | `SELECT` | `resourceGroupName, subscriptionId` | The List VirtualNetworkGatewayConnections operation retrieves all the virtual network gateways connections created. |
| `VirtualNetworkGatewayConnections_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName` | Creates or updates a virtual network gateway connection in the specified resource group. |
| `VirtualNetworkGatewayConnections_Delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName` | Deletes the specified virtual network Gateway connection. |
| `VirtualNetworkGatewayConnections_Get` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName` | Gets the specified virtual network gateway connection by resource group. |
| `VirtualNetworkGatewayConnections_GetIkeSas` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName` | Lists IKE Security Associations for the virtual network gateway connection in the specified resource group. |
| `VirtualNetworkGatewayConnections_GetSharedKey` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName` | The Get VirtualNetworkGatewayConnectionSharedKey operation retrieves information about the specified virtual network gateway connection shared key through Network resource provider. |
| `VirtualNetworkGatewayConnections_ResetConnection` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName` | Resets the virtual network gateway connection specified. |
| `VirtualNetworkGatewayConnections_ResetSharedKey` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName, data__keyLength` | The VirtualNetworkGatewayConnectionResetSharedKey operation resets the virtual network gateway connection shared key for passed virtual network gateway connection in the specified resource group through Network resource provider. |
| `VirtualNetworkGatewayConnections_SetSharedKey` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName, data__value` | The Put VirtualNetworkGatewayConnectionSharedKey operation sets the virtual network gateway connection shared key for passed virtual network gateway connection in the specified resource group through Network resource provider. |
| `VirtualNetworkGatewayConnections_StartPacketCapture` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName` | Starts packet capture on virtual network gateway connection in the specified resource group. |
| `VirtualNetworkGatewayConnections_StopPacketCapture` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName` | Stops packet capture on virtual network gateway connection in the specified resource group. |
| `VirtualNetworkGatewayConnections_UpdateTags` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName` | Updates a virtual network gateway connection tags. |
