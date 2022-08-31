---
title: deleted_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_servers
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
<tr><td><b>Name</b></td><td><code>deleted_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.deleted_servers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `deletionTime` | `string` | The deletion time of the deleted server. |
| `fullyQualifiedDomainName` | `string` | The fully qualified domain name of the server. |
| `originalId` | `string` | The original ID of the server before deletion. |
| `version` | `string` | The version of the deleted server. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DeletedServers_List` | `SELECT` | `subscriptionId` | Gets a list of all deleted servers in a subscription. |
| `DeletedServers_ListByLocation` | `SELECT` | `locationName, subscriptionId` | Gets a list of deleted servers for a location. |
| `DeletedServers_Get` | `EXEC` | `deletedServerName, locationName, subscriptionId` | Gets a deleted server. |
| `DeletedServers_Recover` | `EXEC` | `deletedServerName, locationName, subscriptionId` | Recovers a deleted server. |
