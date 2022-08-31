---
title: virtual_hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_hubs
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
<tr><td><b>Name</b></td><td><code>virtual_hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_hubs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `securityProviderName` | `string` | The Security Provider name. |
| `routingState` | `string` | The current routing state of the VirtualHub. |
| `azureFirewall` | `object` | Reference to another subresource. |
| `tags` | `object` | Resource tags. |
| `virtualRouterIps` | `array` | VirtualRouter IPs. |
| `virtualRouterAsn` | `integer` | VirtualRouter ASN. |
| `hubRoutingPreference` | `string` | The hub routing preference gateway types |
| `p2SVpnGateway` | `object` | Reference to another subresource. |
| `ipConfigurations` | `array` | List of references to IpConfigurations. |
| `provisioningState` | `string` | The current provisioning state. |
| `location` | `string` | Resource location. |
| `virtualRouterAutoScaleConfiguration` | `object` | The VirtualHub Router autoscale configuration. |
| `bgpConnections` | `array` | List of references to Bgp Connections. |
| `type` | `string` | Resource type. |
| `vpnGateway` | `object` | Reference to another subresource. |
| `sku` | `string` | The sku of this VirtualHub. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `virtualHubRouteTableV2s` | `array` | List of all virtual hub route table v2s associated with this VirtualHub. |
| `allowBranchToBranchTraffic` | `boolean` | Flag to control transit for VirtualRouter hub. |
| `addressPrefix` | `string` | Address-prefix for this VirtualHub. |
| `preferredRoutingGateway` | `string` | The preferred routing gateway types |
| `virtualWan` | `object` | Reference to another subresource. |
| `routeTable` | `object` | VirtualHub route table. |
| `securityPartnerProvider` | `object` | Reference to another subresource. |
| `expressRouteGateway` | `object` | Reference to another subresource. |
| `kind` | `string` | Kind of service virtual hub. This is metadata used for the Azure portal experience for Route Server. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualHubs_List` | `SELECT` | `subscriptionId` | Lists all the VirtualHubs in a subscription. |
| `VirtualHubs_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the VirtualHubs in a resource group. |
| `VirtualHubs_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, virtualHubName, data__location` | Creates a VirtualHub resource if it doesn't exist else updates the existing VirtualHub. |
| `VirtualHubs_Delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualHubName` | Deletes a VirtualHub. |
| `VirtualHubs_Get` | `EXEC` | `resourceGroupName, subscriptionId, virtualHubName` | Retrieves the details of a VirtualHub. |
| `VirtualHubs_GetEffectiveVirtualHubRoutes` | `EXEC` | `resourceGroupName, subscriptionId, virtualHubName` | Gets the effective routes configured for the Virtual Hub resource or the specified resource . |
| `VirtualHubs_UpdateTags` | `EXEC` | `resourceGroupName, subscriptionId, virtualHubName` | Updates VirtualHub tags. |
