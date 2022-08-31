---
title: protection_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - protection_containers
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
<tr><td><b>Name</b></td><td><code>protection_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_backup.protection_containers</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ProtectionContainers_Get` | `EXEC` | `api-version, containerName, fabricName, resourceGroupName, subscriptionId, vaultName` | Gets details of the specific container registered to your Recovery Services Vault. |
| `ProtectionContainers_Inquire` | `EXEC` | `api-version, containerName, fabricName, resourceGroupName, subscriptionId, vaultName` | This is an async operation and the results should be tracked using location header or Azure-async-url. |
| `ProtectionContainers_Refresh` | `EXEC` | `api-version, fabricName, resourceGroupName, subscriptionId, vaultName` | Discovers all the containers in the subscription that can be backed up to Recovery Services Vault. This is an
| `ProtectionContainers_Register` | `EXEC` | `api-version, containerName, fabricName, resourceGroupName, subscriptionId, vaultName` | Registers the container with Recovery Services vault.
| `ProtectionContainers_Unregister` | `EXEC` | `api-version, containerName, fabricName, resourceGroupName, subscriptionId, vaultName` | Unregisters the given container from your Recovery Services Vault. This is an asynchronous operation. To determine