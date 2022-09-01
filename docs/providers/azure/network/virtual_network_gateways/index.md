---
title: virtual_network_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_gateways
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
<tr><td><b>Name</b></td><td><code>virtual_network_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_network_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `enablePrivateIpAddress` | `boolean` | Whether private IP needs to be enabled on this gateway for connections or not. |
| `gatewayDefaultSite` | `object` | Reference to another subresource. |
| `enableBgp` | `boolean` | Whether BGP is enabled for this virtual network gateway or not. |
| `vpnType` | `string` | The type of this virtual network gateway. |
| `type` | `string` | Resource type. |
| `natRules` | `array` | NatRules for virtual network gateway. |
| `resourceGuid` | `string` | The resource GUID property of the virtual network gateway resource. |
| `location` | `string` | Resource location. |
| `customRoutes` | `object` | AddressSpace contains an array of IP address ranges that can be used by subnets of the virtual network. |
| `vpnGatewayGeneration` | `string` | The generation for this VirtualNetworkGateway. Must be None if gatewayType is not VPN. |
| `tags` | `object` | Resource tags. |
| `ipConfigurations` | `array` | IP configurations for virtual network gateway. |
| `inboundDnsForwardingEndpoint` | `string` | The IP address allocated by the gateway to which dns requests can be sent. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `vpnClientConfiguration` | `object` | VpnClientConfiguration for P2S client. |
| `sku` | `object` | VirtualNetworkGatewaySku details. |
| `activeActive` | `boolean` | ActiveActive flag. |
| `disableIPSecReplayProtection` | `boolean` | disableIPSecReplayProtection flag. |
| `enableBgpRouteTranslationForNat` | `boolean` | EnableBgpRouteTranslationForNat flag. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `provisioningState` | `string` | The current provisioning state. |
| `enableDnsForwarding` | `boolean` | Whether dns forwarding is enabled or not. |
| `vNetExtendedLocationResourceId` | `string` | Customer vnet resource id. VirtualNetworkGateway of type local gateway is associated with the customer vnet. |
| `gatewayType` | `string` | The type of this virtual network gateway. |
| `bgpSettings` | `object` | BGP settings details. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualNetworkGateways_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all virtual network gateways by resource group. |
| `VirtualNetworkGateways_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Creates or updates a virtual network gateway in the specified resource group. |
| `VirtualNetworkGateways_Delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Deletes the specified virtual network gateway. |
| `VirtualNetworkGateways_DisconnectVirtualNetworkGatewayVpnConnections` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Disconnect vpn connections of virtual network gateway in the specified resource group. |
| `VirtualNetworkGateways_GenerateVpnProfile` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Generates VPN profile for P2S client of the virtual network gateway in the specified resource group. Used for IKEV2 and radius based authentication. |
| `VirtualNetworkGateways_Generatevpnclientpackage` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Generates VPN client package for P2S client of the virtual network gateway in the specified resource group. |
| `VirtualNetworkGateways_Get` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Gets the specified virtual network gateway by resource group. |
| `VirtualNetworkGateways_GetAdvertisedRoutes` | `EXEC` | `peer, resourceGroupName, subscriptionId, virtualNetworkGatewayName` | This operation retrieves a list of routes the virtual network gateway is advertising to the specified peer. |
| `VirtualNetworkGateways_GetBgpPeerStatus` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | The GetBgpPeerStatus operation retrieves the status of all BGP peers. |
| `VirtualNetworkGateways_GetLearnedRoutes` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | This operation retrieves a list of routes the virtual network gateway has learned, including routes learned from BGP peers. |
| `VirtualNetworkGateways_GetVpnProfilePackageUrl` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Gets pre-generated VPN profile for P2S client of the virtual network gateway in the specified resource group. The profile needs to be generated first using generateVpnProfile. |
| `VirtualNetworkGateways_GetVpnclientConnectionHealth` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Get VPN client connection health detail per P2S client connection of the virtual network gateway in the specified resource group. |
| `VirtualNetworkGateways_GetVpnclientIpsecParameters` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | The Get VpnclientIpsecParameters operation retrieves information about the vpnclient ipsec policy for P2S client of virtual network gateway in the specified resource group through Network resource provider. |
| `VirtualNetworkGateways_ListConnections` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Gets all the connections in a virtual network gateway. |
| `VirtualNetworkGateways_Reset` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Resets the primary of the virtual network gateway in the specified resource group. |
| `VirtualNetworkGateways_ResetVpnClientSharedKey` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Resets the VPN client shared key of the virtual network gateway in the specified resource group. |
| `VirtualNetworkGateways_SetVpnclientIpsecParameters` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName, data__dhGroup, data__ikeEncryption, data__ikeIntegrity, data__ipsecEncryption, data__ipsecIntegrity, data__pfsGroup, data__saDataSizeKilobytes, data__saLifeTimeSeconds` | The Set VpnclientIpsecParameters operation sets the vpnclient ipsec policy for P2S client of virtual network gateway in the specified resource group through Network resource provider. |
| `VirtualNetworkGateways_StartPacketCapture` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Starts packet capture on virtual network gateway in the specified resource group. |
| `VirtualNetworkGateways_StopPacketCapture` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Stops packet capture on virtual network gateway in the specified resource group. |
| `VirtualNetworkGateways_SupportedVpnDevices` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Gets a xml format representation for supported vpn devices. |
| `VirtualNetworkGateways_UpdateTags` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Updates a virtual network gateway tags. |
| `VirtualNetworkGateways_VpnDeviceConfigurationScript` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName` | Gets a xml format representation for vpn device configuration script. |
