---
title: subscription_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_usages
  - sql
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
<tr><td><b>Name</b></td><td><code>subscription_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.subscription_usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unit` | `string` | Unit of the metric. |
| `currentValue` | `number` | Current value of the metric. |
| `displayName` | `string` | User-readable name of the metric. |
| `limit` | `number` | Boundary value of the metric. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SubscriptionUsages_ListByLocation` | `SELECT` | `locationName, subscriptionId` | Gets all subscription usage metrics in a given location. |
| `SubscriptionUsages_Get` | `EXEC` | `locationName, subscriptionId, usageName` | Gets a subscription usage metric. |
