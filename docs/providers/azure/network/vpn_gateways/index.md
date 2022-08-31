---
title: vpn_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_gateways
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
<tr><td><b>Name</b></td><td><code>vpn_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.vpn_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `bgpSettings` | `object` | BGP settings details. |
| `virtualHub` | `object` | Reference to another subresource. |
| `type` | `string` | Resource type. |
| `vpnGatewayScaleUnit` | `integer` | The scale unit for this vpn gateway. |
| `isRoutingPreferenceInternet` | `boolean` | Enable Routing Preference property for the Public IP Interface of the VpnGateway. |
| `enableBgpRouteTranslationForNat` | `boolean` | Enable BGP routes translation for NAT on this VpnGateway. |
| `natRules` | `array` | List of all the nat Rules associated with the gateway. |
| `tags` | `object` | Resource tags. |
| `provisioningState` | `string` | The current provisioning state. |
| `ipConfigurations` | `array` | List of all IPs configured on the gateway. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `connections` | `array` | List of all vpn connections to the gateway. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VpnGateways_List` | `SELECT` | `subscriptionId` | Lists all the VpnGateways in a subscription. |
| `VpnGateways_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the VpnGateways in a resource group. |
| `VpnGateways_CreateOrUpdate` | `INSERT` | `gatewayName, resourceGroupName, subscriptionId, data__location` | Creates a virtual wan vpn gateway if it doesn't exist else updates the existing gateway. |
| `VpnGateways_Delete` | `DELETE` | `gatewayName, resourceGroupName, subscriptionId` | Deletes a virtual wan vpn gateway. |
| `VpnGateways_Get` | `EXEC` | `gatewayName, resourceGroupName, subscriptionId` | Retrieves the details of a virtual wan vpn gateway. |
| `VpnGateways_Reset` | `EXEC` | `gatewayName, resourceGroupName, subscriptionId` | Resets the primary of the vpn gateway in the specified resource group. |
| `VpnGateways_StartPacketCapture` | `EXEC` | `gatewayName, resourceGroupName, subscriptionId` | Starts packet capture on vpn gateway in the specified resource group. |
| `VpnGateways_StopPacketCapture` | `EXEC` | `gatewayName, resourceGroupName, subscriptionId` | Stops packet capture on vpn gateway in the specified resource group. |
| `VpnGateways_UpdateTags` | `EXEC` | `gatewayName, resourceGroupName, subscriptionId` | Updates virtual wan vpn gateway tags. |
