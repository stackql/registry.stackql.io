---
title: express_route_cross_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_cross_connections
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
<tr><td><b>Name</b></td><td><code>express_route_cross_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.express_route_cross_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `location` | `string` | Resource location. |
| `tags` | `object` | Resource tags. |
| `peerings` | `array` | The list of peerings. |
| `bandwidthInMbps` | `integer` | The circuit bandwidth In Mbps. |
| `primaryAzurePort` | `string` | The name of the primary port. |
| `expressRouteCircuit` | `object` | Reference to an express route circuit. |
| `secondaryAzurePort` | `string` | The name of the secondary port. |
| `serviceProviderNotes` | `string` | Additional read only notes set by the connectivity provider. |
| `serviceProviderProvisioningState` | `string` | The ServiceProviderProvisioningState state of the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `type` | `string` | Resource type. |
| `sTag` | `integer` | The identifier of the circuit traffic. |
| `peeringLocation` | `string` | The peering location of the ExpressRoute circuit. |
| `provisioningState` | `string` | The current provisioning state. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ExpressRouteCrossConnections_List` | `SELECT` | `subscriptionId` | Retrieves all the ExpressRouteCrossConnections in a subscription. |
| `ExpressRouteCrossConnections_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieves all the ExpressRouteCrossConnections in a resource group. |
| `ExpressRouteCrossConnections_CreateOrUpdate` | `INSERT` | `crossConnectionName, resourceGroupName, subscriptionId` | Update the specified ExpressRouteCrossConnection. |
| `ExpressRouteCrossConnections_Get` | `EXEC` | `crossConnectionName, resourceGroupName, subscriptionId` | Gets details about the specified ExpressRouteCrossConnection. |
| `ExpressRouteCrossConnections_ListArpTable` | `EXEC` | `crossConnectionName, devicePath, peeringName, resourceGroupName, subscriptionId` | Gets the currently advertised ARP table associated with the express route cross connection in a resource group. |
| `ExpressRouteCrossConnections_ListRoutesTable` | `EXEC` | `crossConnectionName, devicePath, peeringName, resourceGroupName, subscriptionId` | Gets the currently advertised routes table associated with the express route cross connection in a resource group. |
| `ExpressRouteCrossConnections_ListRoutesTableSummary` | `EXEC` | `crossConnectionName, devicePath, peeringName, resourceGroupName, subscriptionId` | Gets the route table summary associated with the express route cross connection in a resource group. |
| `ExpressRouteCrossConnections_UpdateTags` | `EXEC` | `crossConnectionName, resourceGroupName, subscriptionId` | Updates an express route cross connection tags. |