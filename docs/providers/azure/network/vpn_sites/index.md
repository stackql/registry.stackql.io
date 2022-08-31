---
title: vpn_sites
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_sites
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
<tr><td><b>Name</b></td><td><code>vpn_sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.vpn_sites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `deviceProperties` | `object` | List of properties of the device. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `tags` | `object` | Resource tags. |
| `bgpProperties` | `object` | BGP settings details. |
| `isSecuritySite` | `boolean` | IsSecuritySite flag. |
| `virtualWan` | `object` | Reference to another subresource. |
| `vpnSiteLinks` | `array` | List of all vpn site links. |
| `o365Policy` | `object` | The Office365 breakout policy. |
| `location` | `string` | Resource location. |
| `provisioningState` | `string` | The current provisioning state. |
| `type` | `string` | Resource type. |
| `ipAddress` | `string` | The ip-address for the vpn-site. |
| `addressSpace` | `object` | AddressSpace contains an array of IP address ranges that can be used by subnets of the virtual network. |
| `siteKey` | `string` | The key for vpn-site that can be used for connections. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VpnSites_List` | `SELECT` | `subscriptionId` | Lists all the VpnSites in a subscription. |
| `VpnSites_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the vpnSites in a resource group. |
| `VpnSites_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, vpnSiteName, data__location` | Creates a VpnSite resource if it doesn't exist else updates the existing VpnSite. |
| `VpnSites_Delete` | `DELETE` | `resourceGroupName, subscriptionId, vpnSiteName` | Deletes a VpnSite. |
| `VpnSites_Get` | `EXEC` | `resourceGroupName, subscriptionId, vpnSiteName` | Retrieves the details of a VPN site. |
| `VpnSites_UpdateTags` | `EXEC` | `resourceGroupName, subscriptionId, vpnSiteName` | Updates VpnSite tags. |