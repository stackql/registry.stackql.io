---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - postgresql_hsc
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
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.postgresql_hsc.servers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `fullyQualifiedDomainName` | `string` | The fully qualified domain name of a server. |
| `standbyAvailabilityZone` | `string` | Standby Availability Zone information of the server group. |
| `postgresqlVersion` | `string` | The PostgreSQL version. |
| `citusVersion` | `string` | The Citus version. |
| `administratorLogin` | `string` | The administrator's login name of a servers in server group. |
| `availabilityZone` | `string` | Availability Zone information of the server group. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `role` | `string` | The role of a server. |
| `haState` | `string` | A state of a server role group/server that is visible to user for HA feature. |
| `state` | `string` | A state of a server group/server that is visible to user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Servers_ListByServerGroup` | `SELECT` | `resourceGroupName, serverGroupName, subscriptionId` | Lists servers of a server group. |
| `Servers_Get` | `EXEC` | `resourceGroupName, serverGroupName, serverName, subscriptionId` | Gets information about a server in server group. |
