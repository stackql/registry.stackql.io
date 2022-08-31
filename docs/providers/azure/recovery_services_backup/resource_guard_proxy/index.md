---
title: resource_guard_proxy
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_guard_proxy
  - recovery_services_backup
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
<tr><td><b>Name</b></td><td><code>resource_guard_proxy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_backup.resource_guard_proxy</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ResourceGuardProxy_Delete` | `DELETE` | `api-version, resourceGroupName, resourceGuardProxyName, subscriptionId, vaultName` | Delete ResourceGuardProxy under vault |
| `ResourceGuardProxy_Get` | `EXEC` | `api-version, resourceGroupName, resourceGuardProxyName, subscriptionId, vaultName` | Returns ResourceGuardProxy under vault and with the name referenced in request |
| `ResourceGuardProxy_Put` | `EXEC` | `api-version, resourceGroupName, resourceGuardProxyName, subscriptionId, vaultName` | Add or Update ResourceGuardProxy under vault<br />Secures vault critical operations |
| `ResourceGuardProxy_UnlockDelete` | `EXEC` | `api-version, resourceGroupName, resourceGuardProxyName, subscriptionId, vaultName` | Secures delete ResourceGuardProxy operations. |
