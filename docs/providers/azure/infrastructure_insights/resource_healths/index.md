---
title: resource_healths
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_healths
  - infrastructure_insights
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
<tr><td><b>Name</b></td><td><code>resource_healths</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.infrastructure_insights.resource_healths</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `rpRegistrationId` | `string` | Gets or sets the resource provider registration ID. |
| `resourceName` | `string` | Resource name. |
| `resourceURI` | `string` | Gets or sets the resource URI. |
| `tags` | `object` | Resource tags. |
| `usageMetrics` | `array` | Usage metrics. |
| `resourceType` | `string` | Resource type. |
| `resourceDisplayName` | `string` | Resource display name. |
| `location` | `string` | The Azure Region where the resource lives |
| `resourceLocation` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ResourceHealths_List` | `SELECT` | `location, resourceGroupName, serviceRegistrationId, subscriptionId` | Returns a list of each resource's health under a service. |
| `ResourceHealths_Get` | `EXEC` | `location, resourceGroupName, resourceRegistrationId, serviceRegistrationId, subscriptionId` | Returns the requested health information about a resource. |
