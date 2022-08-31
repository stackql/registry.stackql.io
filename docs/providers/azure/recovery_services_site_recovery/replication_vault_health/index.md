---
title: replication_vault_health
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_vault_health
  - recovery_services_site_recovery
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
<tr><td><b>Name</b></td><td><code>replication_vault_health</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.replication_vault_health</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReplicationVaultHealth_Get` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | Gets the health details of the vault. |
| `ReplicationVaultHealth_Refresh` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` |  |
