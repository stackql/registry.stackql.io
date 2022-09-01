---
title: express_route_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_connections
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
<tr><td><b>Name</b></td><td><code>express_route_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.express_route_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource. |
| `expressRouteCircuitPeering` | `object` | ExpressRoute circuit peering identifier. |
| `routingWeight` | `integer` | The routing weight associated to the connection. |
| `expressRouteGatewayBypass` | `boolean` | Enable FastPath to vWan Firewall hub. |
| `enableInternetSecurity` | `boolean` | Enable internet security. |
| `routingConfiguration` | `object` | Routing Configuration indicating the associated and propagated route tables for this connection. |
| `provisioningState` | `string` | The current provisioning state. |
| `authorizationKey` | `string` | Authorization key to establish the connection. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ExpressRouteConnections_List` | `SELECT` | `expressRouteGatewayName, resourceGroupName, subscriptionId` | Lists ExpressRouteConnections. |
| `ExpressRouteConnections_CreateOrUpdate` | `INSERT` | `connectionName, expressRouteGatewayName, resourceGroupName, subscriptionId, data__name` | Creates a connection between an ExpressRoute gateway and an ExpressRoute circuit. |
| `ExpressRouteConnections_Delete` | `DELETE` | `connectionName, expressRouteGatewayName, resourceGroupName, subscriptionId` | Deletes a connection to a ExpressRoute circuit. |
| `ExpressRouteConnections_Get` | `EXEC` | `connectionName, expressRouteGatewayName, resourceGroupName, subscriptionId` | Gets the specified ExpressRouteConnection. |
