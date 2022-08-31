---
title: backup_vaults
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_vaults
  - data_protection
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
<tr><td><b>Name</b></td><td><code>backup_vaults</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_protection.backup_vaults</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BackupVaults_CreateOrUpdate` | `INSERT` | `api-version, resourceGroupName, subscriptionId, vaultName, data__location, data__properties` | Creates or updates a BackupVault resource belonging to a resource group. |
| `BackupVaults_Delete` | `DELETE` | `api-version, resourceGroupName, subscriptionId, vaultName` | Deletes a BackupVault resource from the resource group. |
| `BackupVaults_CheckNameAvailability` | `EXEC` | `api-version, location, resourceGroupName, subscriptionId` |  |
| `BackupVaults_Get` | `EXEC` | `api-version, resourceGroupName, subscriptionId, vaultName` | Returns a resource belonging to a resource group. |
| `BackupVaults_GetInResourceGroup` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | Returns resource collection belonging to a resource group. |
| `BackupVaults_GetInSubscription` | `EXEC` | `api-version, subscriptionId` | Returns resource collection belonging to a subscription. |
| `BackupVaults_Update` | `EXEC` | `api-version, resourceGroupName, subscriptionId, vaultName` | Updates a BackupVault resource belonging to a resource group. For example, updating tags for a resource. |
