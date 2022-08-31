---
title: express_route_ports
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_ports
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
<tr><td><b>Name</b></td><td><code>express_route_ports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.express_route_ports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `mtu` | `string` | Maximum transmission unit of the physical port pair(s). |
| `allocationDate` | `string` | Date of the physical port allocation to be used in Letter of Authorization. |
| `etherType` | `string` | Ether type of the physical port. |
| `location` | `string` | Resource location. |
| `provisionedBandwidthInGbps` | `number` | Aggregate Gbps of associated circuit bandwidths. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `resourceGuid` | `string` | The resource GUID property of the express route port resource. |
| `bandwidthInGbps` | `integer` | Bandwidth of procured ports in Gbps. |
| `peeringLocation` | `string` | The name of the peering location that the ExpressRoutePort is mapped to physically. |
| `provisioningState` | `string` | The current provisioning state. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `circuits` | `array` | Reference the ExpressRoute circuit(s) that are provisioned on this ExpressRoutePort resource. |
| `identity` | `object` | Identity for the resource. |
| `encapsulation` | `string` | Encapsulation method on physical ports. |
| `links` | `array` | The set of physical links of the ExpressRoutePort resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ExpressRoutePorts_List` | `SELECT` | `subscriptionId` | List all the ExpressRoutePort resources in the specified subscription. |
| `ExpressRoutePorts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all the ExpressRoutePort resources in the specified resource group. |
| `ExpressRoutePorts_CreateOrUpdate` | `INSERT` | `expressRoutePortName, resourceGroupName, subscriptionId` | Creates or updates the specified ExpressRoutePort resource. |
| `ExpressRoutePorts_Delete` | `DELETE` | `expressRoutePortName, resourceGroupName, subscriptionId` | Deletes the specified ExpressRoutePort resource. |
| `ExpressRoutePorts_GenerateLOA` | `EXEC` | `expressRoutePortName, resourceGroupName, subscriptionId, data__customerName` | Generate a letter of authorization for the requested ExpressRoutePort resource. |
| `ExpressRoutePorts_Get` | `EXEC` | `expressRoutePortName, resourceGroupName, subscriptionId` | Retrieves the requested ExpressRoutePort resource. |
| `ExpressRoutePorts_UpdateTags` | `EXEC` | `expressRoutePortName, resourceGroupName, subscriptionId` | Update ExpressRoutePort tags. |
