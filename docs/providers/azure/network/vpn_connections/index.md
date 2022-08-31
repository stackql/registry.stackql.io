---
title: vpn_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_connections
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
<tr><td><b>Name</b></td><td><code>vpn_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.vpn_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `enableInternetSecurity` | `boolean` | Enable internet security. |
| `dpdTimeoutSeconds` | `integer` | DPD timeout in seconds for vpn connection. |
| `useLocalAzureIpAddress` | `boolean` | Use local azure ip to initiate connection. |
| `enableRateLimiting` | `boolean` | EnableBgp flag. |
| `egressBytesTransferred` | `integer` | Egress bytes transferred. |
| `vpnConnectionProtocolType` | `string` | Gateway connection protocol. |
| `connectionStatus` | `string` | The current state of the vpn connection. |
| `enableBgp` | `boolean` | EnableBgp flag. |
| `routingConfiguration` | `object` | Routing Configuration indicating the associated and propagated route tables for this connection. |
| `routingWeight` | `integer` | Routing weight for vpn connection. |
| `vpnLinkConnections` | `array` | List of all vpn site link connections to the gateway. |
| `remoteVpnSite` | `object` | Reference to another subresource. |
| `sharedKey` | `string` | SharedKey for the vpn connection. |
| `usePolicyBasedTrafficSelectors` | `boolean` | Enable policy-based traffic selectors. |
| `connectionBandwidth` | `integer` | Expected bandwidth in MBPS. |
| `trafficSelectorPolicies` | `array` | The Traffic Selector Policies to be considered by this connection. |
| `ingressBytesTransferred` | `integer` | Ingress bytes transferred. |
| `provisioningState` | `string` | The current provisioning state. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `ipsecPolicies` | `array` | The IPSec Policies to be considered by this connection. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VpnConnections_ListByVpnGateway` | `SELECT` | `gatewayName, resourceGroupName, subscriptionId` | Retrieves all vpn connections for a particular virtual wan vpn gateway. |
| `VpnConnections_CreateOrUpdate` | `INSERT` | `connectionName, gatewayName, resourceGroupName, subscriptionId` | Creates a vpn connection to a scalable vpn gateway if it doesn't exist else updates the existing connection. |
| `VpnConnections_Delete` | `DELETE` | `connectionName, gatewayName, resourceGroupName, subscriptionId` | Deletes a vpn connection. |
| `VpnConnections_Get` | `EXEC` | `connectionName, gatewayName, resourceGroupName, subscriptionId` | Retrieves the details of a vpn connection. |
| `VpnConnections_StartPacketCapture` | `EXEC` | `gatewayName, resourceGroupName, subscriptionId, vpnConnectionName` | Starts packet capture on Vpn connection in the specified resource group. |
| `VpnConnections_StopPacketCapture` | `EXEC` | `gatewayName, resourceGroupName, subscriptionId, vpnConnectionName` | Stops packet capture on Vpn connection in the specified resource group. |
