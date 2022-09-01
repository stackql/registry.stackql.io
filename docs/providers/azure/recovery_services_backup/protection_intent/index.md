---
title: protection_intent
hide_title: false
hide_table_of_contents: false
keywords:
  - protection_intent
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
<tr><td><b>Name</b></td><td><code>protection_intent</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_backup.protection_intent</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ProtectionIntent_CreateOrUpdate` | `INSERT` | `api-version, fabricName, intentObjectName, resourceGroupName, subscriptionId, vaultName` | Create Intent for Enabling backup of an item. This is a synchronous operation. |
| `ProtectionIntent_Delete` | `DELETE` | `api-version, fabricName, intentObjectName, resourceGroupName, subscriptionId, vaultName` | Used to remove intent from an item |
| `ProtectionIntent_Get` | `EXEC` | `api-version, fabricName, intentObjectName, resourceGroupName, subscriptionId, vaultName` | Provides the details of the protection intent up item. This is an asynchronous operation. To know the status of the operation,<br />call the GetItemOperationResult API. |
| `ProtectionIntent_Validate` | `EXEC` | `api-version, azureRegion, subscriptionId` |  |
