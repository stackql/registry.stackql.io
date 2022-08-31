---
title: protected_items
hide_title: false
hide_table_of_contents: false
keywords:
  - protected_items
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
<tr><td><b>Name</b></td><td><code>protected_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_backup.protected_items</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ProtectedItems_CreateOrUpdate` | `INSERT` | `api-version, containerName, fabricName, protectedItemName, resourceGroupName, subscriptionId, vaultName` | Enables backup of an item or to modifies the backup policy information of an already backed up item. This is an
| `ProtectedItems_Delete` | `DELETE` | `api-version, containerName, fabricName, protectedItemName, resourceGroupName, subscriptionId, vaultName` | Used to disable backup of an item within a container. This is an asynchronous operation. To know the status of the
| `ProtectedItems_Get` | `EXEC` | `api-version, containerName, fabricName, protectedItemName, resourceGroupName, subscriptionId, vaultName` | Provides the details of the backed up item. This is an asynchronous operation. To know the status of the operation,