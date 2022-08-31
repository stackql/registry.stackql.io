---
title: route_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - route_tables
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
<tr><td><b>Name</b></td><td><code>route_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.route_tables</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `resourceGuid` | `string` | The resource GUID property of the route table. |
| `disableBgpRoutePropagation` | `boolean` | Whether to disable the routes learned by BGP on that route table. True means disable. |
| `location` | `string` | Resource location. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `routes` | `array` | Collection of routes contained within a route table. |
| `type` | `string` | Resource type. |
| `provisioningState` | `string` | The current provisioning state. |
| `tags` | `object` | Resource tags. |
| `subnets` | `array` | A collection of references to subnets. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RouteTables_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all route tables in a resource group. |
| `RouteTables_ListAll` | `SELECT` | `subscriptionId` | Gets all route tables in a subscription. |
| `RouteTables_CreateOrUpdate` | `INSERT` | `resourceGroupName, routeTableName, subscriptionId` | Create or updates a route table in a specified resource group. |
| `RouteTables_Delete` | `DELETE` | `resourceGroupName, routeTableName, subscriptionId` | Deletes the specified route table. |
| `RouteTables_Get` | `EXEC` | `resourceGroupName, routeTableName, subscriptionId` | Gets the specified route table. |
| `RouteTables_UpdateTags` | `EXEC` | `resourceGroupName, routeTableName, subscriptionId` | Updates a route table tags. |
