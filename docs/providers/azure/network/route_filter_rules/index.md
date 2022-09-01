---
title: route_filter_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - route_filter_rules
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
<tr><td><b>Name</b></td><td><code>route_filter_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.route_filter_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `provisioningState` | `string` | The current provisioning state. |
| `routeFilterRuleType` | `string` | The rule type of the rule. |
| `access` | `string` | Access to be allowed or denied. |
| `communities` | `array` | The collection for bgp community values to filter on. e.g. ['12076:5010','12076:5020']. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RouteFilterRules_ListByRouteFilter` | `SELECT` | `resourceGroupName, routeFilterName, subscriptionId` | Gets all RouteFilterRules in a route filter. |
| `RouteFilterRules_CreateOrUpdate` | `INSERT` | `resourceGroupName, routeFilterName, ruleName, subscriptionId` | Creates or updates a route in the specified route filter. |
| `RouteFilterRules_Delete` | `DELETE` | `resourceGroupName, routeFilterName, ruleName, subscriptionId` | Deletes the specified rule from a route filter. |
| `RouteFilterRules_Get` | `EXEC` | `resourceGroupName, routeFilterName, ruleName, subscriptionId` | Gets the specified rule from a route filter. |
