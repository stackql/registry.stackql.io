---
title: i_pv6_firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - i_pv6_firewall_rules
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
<tr><td><b>Name</b></td><td><code>i_pv6_firewall_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.i_pv6_firewall_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `endIPv6Address` | `string` | The end IP address of the firewall rule. Must be IPv6 format. Must be greater than or equal to startIpAddress. |
| `startIPv6Address` | `string` | The start IP address of the firewall rule. Must be IPv6 format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IPv6FirewallRules_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of IPv6 firewall rules. |
| `IPv6FirewallRules_CreateOrUpdate` | `INSERT` | `firewallRuleName, resourceGroupName, serverName, subscriptionId` | Creates or updates an IPv6 firewall rule. |
| `IPv6FirewallRules_Delete` | `DELETE` | `firewallRuleName, resourceGroupName, serverName, subscriptionId` | Deletes an IPv6 firewall rule. |
| `IPv6FirewallRules_Get` | `EXEC` | `firewallRuleName, resourceGroupName, serverName, subscriptionId` | Gets an IPv6 firewall rule. |