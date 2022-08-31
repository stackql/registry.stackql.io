---
title: server_trust_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - server_trust_groups
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
<tr><td><b>Name</b></td><td><code>server_trust_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.server_trust_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `groupMembers` | `array` | Group members information for the server trust group. |
| `trustScopes` | `array` | Trust scope of the server trust group. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerTrustGroups_ListByInstance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a server trust groups by instance name. |
| `ServerTrustGroups_ListByLocation` | `SELECT` | `locationName, resourceGroupName, subscriptionId` | Lists a server trust group. |
| `ServerTrustGroups_CreateOrUpdate` | `INSERT` | `locationName, resourceGroupName, serverTrustGroupName, subscriptionId` | Creates or updates a server trust group. |
| `ServerTrustGroups_Delete` | `DELETE` | `locationName, resourceGroupName, serverTrustGroupName, subscriptionId` | Deletes a server trust group. |
| `ServerTrustGroups_Get` | `EXEC` | `locationName, resourceGroupName, serverTrustGroupName, subscriptionId` | Gets a server trust group. |