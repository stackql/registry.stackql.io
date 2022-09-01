---
title: private_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoints
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
<tr><td><b>Name</b></td><td><code>private_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.private_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `tags` | `object` | Resource tags. |
| `provisioningState` | `string` | The current provisioning state. |
| `privateLinkServiceConnections` | `array` | A grouping of information about the connection to the remote resource. |
| `type` | `string` | Resource type. |
| `location` | `string` | Resource location. |
| `manualPrivateLinkServiceConnections` | `array` | A grouping of information about the connection to the remote resource. Used when the network admin does not have access to approve connections to the remote resource. |
| `applicationSecurityGroups` | `array` | Application security groups in which the private endpoint IP configuration is included. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `ipConfigurations` | `array` | A list of IP configurations of the private endpoint. This will be used to map to the First Party Service's endpoints. |
| `customDnsConfigs` | `array` | An array of custom dns configurations. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `networkInterfaces` | `array` | An array of references to the network interfaces created for this private endpoint. |
| `subnet` | `object` | Subnet in a virtual network resource. |
| `customNetworkInterfaceName` | `string` | The custom name of the network interface attached to the private endpoint. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpoints_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all private endpoints in a resource group. |
| `PrivateEndpoints_ListBySubscription` | `SELECT` | `subscriptionId` | Gets all private endpoints in a subscription. |
| `PrivateEndpoints_CreateOrUpdate` | `INSERT` | `privateEndpointName, resourceGroupName, subscriptionId` | Creates or updates an private endpoint in the specified resource group. |
| `PrivateEndpoints_Delete` | `DELETE` | `privateEndpointName, resourceGroupName, subscriptionId` | Deletes the specified private endpoint. |
| `PrivateEndpoints_Get` | `EXEC` | `privateEndpointName, resourceGroupName, subscriptionId` | Gets the specified private endpoint by resource group. |
