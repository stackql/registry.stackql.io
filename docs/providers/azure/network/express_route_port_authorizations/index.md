---
title: express_route_port_authorizations
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_port_authorizations
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
<tr><td><b>Name</b></td><td><code>express_route_port_authorizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.express_route_port_authorizations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `provisioningState` | `string` | The current provisioning state. |
| `type` | `string` | Type of the resource. |
| `authorizationKey` | `string` | The authorization key. |
| `authorizationUseStatus` | `string` | The authorization use status. |
| `circuitResourceUri` | `string` | The reference to the ExpressRoute circuit resource using the authorization. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ExpressRoutePortAuthorizations_List` | `SELECT` | `expressRoutePortName, resourceGroupName, subscriptionId` | Gets all authorizations in an express route port. |
| `ExpressRoutePortAuthorizations_CreateOrUpdate` | `INSERT` | `authorizationName, expressRoutePortName, resourceGroupName, subscriptionId` | Creates or updates an authorization in the specified express route port. |
| `ExpressRoutePortAuthorizations_Delete` | `DELETE` | `authorizationName, expressRoutePortName, resourceGroupName, subscriptionId` | Deletes the specified authorization from the specified express route port. |
| `ExpressRoutePortAuthorizations_Get` | `EXEC` | `authorizationName, expressRoutePortName, resourceGroupName, subscriptionId` | Gets the specified authorization from the specified express route port. |
