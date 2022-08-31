---
title: vpn_server_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_server_configurations
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
<tr><td><b>Name</b></td><td><code>vpn_server_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.vpn_server_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `vpnClientIpsecPolicies` | `array` | VpnClientIpsecPolicies for VpnServerConfiguration. |
| `configurationPolicyGroups` | `array` | List of all VpnServerConfigurationPolicyGroups. |
| `location` | `string` | Resource location. |
| `tags` | `object` | Resource tags. |
| `vpnClientRootCertificates` | `array` | VPN client root certificate of VpnServerConfiguration. |
| `radiusServers` | `array` | Multiple Radius Server configuration for VpnServerConfiguration. |
| `radiusServerAddress` | `string` | The radius server address property of the VpnServerConfiguration resource for point to site client connection. |
| `aadAuthenticationParameters` | `object` | AAD Vpn authentication type related parameters. |
| `provisioningState` | `string` | The provisioning state of the VpnServerConfiguration resource. Possible values are: 'Updating', 'Deleting', and 'Failed'. |
| `radiusClientRootCertificates` | `array` | Radius client root certificate of VpnServerConfiguration. |
| `p2SVpnGateways` | `array` | List of references to P2SVpnGateways. |
| `vpnClientRevokedCertificates` | `array` | VPN client revoked certificate of VpnServerConfiguration. |
| `vpnProtocols` | `array` | VPN protocols for the VpnServerConfiguration. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `type` | `string` | Resource type. |
| `radiusServerRootCertificates` | `array` | Radius Server root certificate of VpnServerConfiguration. |
| `vpnAuthenticationTypes` | `array` | VPN authentication types for the VpnServerConfiguration. |
| `radiusServerSecret` | `string` | The radius secret property of the VpnServerConfiguration resource for point to site client connection. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VpnServerConfigurations_List` | `SELECT` | `subscriptionId` | Lists all the VpnServerConfigurations in a subscription. |
| `VpnServerConfigurations_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the vpnServerConfigurations in a resource group. |
| `VpnServerConfigurations_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, vpnServerConfigurationName` | Creates a VpnServerConfiguration resource if it doesn't exist else updates the existing VpnServerConfiguration. |
| `VpnServerConfigurations_Delete` | `DELETE` | `resourceGroupName, subscriptionId, vpnServerConfigurationName` | Deletes a VpnServerConfiguration. |
| `VpnServerConfigurations_Get` | `EXEC` | `resourceGroupName, subscriptionId, vpnServerConfigurationName` | Retrieves the details of a VpnServerConfiguration. |
| `VpnServerConfigurations_UpdateTags` | `EXEC` | `resourceGroupName, subscriptionId, vpnServerConfigurationName` | Updates VpnServerConfiguration tags. |