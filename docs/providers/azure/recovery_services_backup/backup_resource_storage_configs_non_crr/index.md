---
title: backup_resource_storage_configs_non_crr
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_resource_storage_configs_non_crr
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
<tr><td><b>Name</b></td><td><code>backup_resource_storage_configs_non_crr</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_backup.backup_resource_storage_configs_non_crr</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BackupResourceStorageConfigsNonCRR_Get` | `EXEC` | `api-version, resourceGroupName, subscriptionId, vaultName` | Fetches resource storage config. |
| `BackupResourceStorageConfigsNonCRR_Update` | `EXEC` | `api-version, resourceGroupName, subscriptionId, vaultName` | Updates vault storage model type. |
| `BackupResourceStorageConfigsNonCRR_patch` | `EXEC` | `api-version, resourceGroupName, subscriptionId, vaultName` | Updates vault storage model type. |