---
title: firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_rules
  - redis
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
<tr><td><b>Name</b></td><td><code>firewall_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.redis.firewall_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `endIP` | `string` | highest IP address included in the range |
| `startIP` | `string` | lowest IP address included in the range |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `FirewallRules_List` | `SELECT` | `cacheName, resourceGroupName, subscriptionId` | Gets all firewall rules in the specified redis cache. |
| `FirewallRules_CreateOrUpdate` | `INSERT` | `cacheName, resourceGroupName, ruleName, subscriptionId` | Create or update a redis cache firewall rule |
| `FirewallRules_Delete` | `DELETE` | `cacheName, resourceGroupName, ruleName, subscriptionId` | Deletes a single firewall rule in a specified redis cache. |
| `FirewallRules_Get` | `EXEC` | `cacheName, resourceGroupName, ruleName, subscriptionId` | Gets a single firewall rule in a specified redis cache. |
