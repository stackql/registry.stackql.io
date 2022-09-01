---
title: route_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - route_filters
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
<tr><td><b>Name</b></td><td><code>route_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.route_filters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `tags` | `object` | Resource tags. |
| `peerings` | `array` | A collection of references to express route circuit peerings. |
| `location` | `string` | Resource location. |
| `ipv6Peerings` | `array` | A collection of references to express route circuit ipv6 peerings. |
| `provisioningState` | `string` | The current provisioning state. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `rules` | `array` | Collection of RouteFilterRules contained within a route filter. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RouteFilters_List` | `SELECT` | `subscriptionId` | Gets all route filters in a subscription. |
| `RouteFilters_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all route filters in a resource group. |
| `RouteFilters_CreateOrUpdate` | `INSERT` | `resourceGroupName, routeFilterName, subscriptionId, data__location` | Creates or updates a route filter in a specified resource group. |
| `RouteFilters_Delete` | `DELETE` | `resourceGroupName, routeFilterName, subscriptionId` | Deletes the specified route filter. |
| `RouteFilters_Get` | `EXEC` | `resourceGroupName, routeFilterName, subscriptionId` | Gets the specified route filter. |
| `RouteFilters_UpdateTags` | `EXEC` | `resourceGroupName, routeFilterName, subscriptionId` | Updates tags of a route filter. |
