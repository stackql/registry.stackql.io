---
title: firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_rules
  - postgresql
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
<tr><td><b>Id</b></td><td><code>azure.postgresql.firewall_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `startIpAddress` | `string` | The start IP address of the server firewall rule. Must be IPv4 format. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `endIpAddress` | `string` | The end IP address of the server firewall rule. Must be IPv4 format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `FirewallRules_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | List all the firewall rules in a given PostgreSQL server. |
| `FirewallRules_CreateOrUpdate` | `INSERT` | `firewallRuleName, resourceGroupName, serverName, subscriptionId` | Creates a new firewall rule or updates an existing firewall rule. |
| `FirewallRules_Delete` | `DELETE` | `firewallRuleName, resourceGroupName, serverName, subscriptionId` | Deletes a PostgreSQL server firewall rule. |
| `FirewallRules_Get` | `EXEC` | `firewallRuleName, resourceGroupName, serverName, subscriptionId` | List all the firewall rules in a given server. |
