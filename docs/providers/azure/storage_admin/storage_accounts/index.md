---
title: storage_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_accounts
  - storage_admin
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
<tr><td><b>Name</b></td><td><code>storage_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_admin.storage_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource Name. |
| `type` | `string` | Resource Type. |
| `primaryLocation` | `string` | The primary location for the storage account. |
| `tenantSubscriptionId` | `string` | Subscription ID of the subscription under which the storage account locates. |
| `accountId` | `string` | Internal storage account ID, which is not visible to tenant. |
| `primaryEndpoints` | `object` | The URLs that are used to perform a retrieval of a public BLOB, queue, or table object. |
| `tenantViewId` | `string` | Resource URI of storage account from tenant view. |
| `creationTime` | `string` | The creation date and time of storage account in UTC. |
| `kind` | `string` | The kind of storage account |
| `supportsHttpsTrafficOnly` | `boolean` | Storage account supports https traffic only or not |
| `encryption` | `object` | Storage encryption setting |
| `provisioningState` | `string` | Storage account state. |
| `healthState` | `string` | Health state for storage account |
| `tenantResourceGroupName` | `string` | The name of resource group under which the storage account locates. |
| `location` | `string` | Resource Location. |
| `accountType` | `string` | Storage account type. |
| `statusOfPrimary` | `string` | Gets the status indicating whether the primary location of the storage account is available or unavailable. |
| `deletedTime` | `string` | The date-time when the storage account was deleted. |
| `tenantStorageAccountName` | `string` | Storage account name from tenant view. |
| `accountStatus` | `string` | The state of storage account in WAC. |
| `faultDomain` | `string` | The fault domain for the storage account. |
| `tags` | `object` | Resource tags. |
| `accessTier` | `string` | Access tier for storage account |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `StorageAccounts_List` | `SELECT` | `location, subscriptionId` | Returns a list of storage accounts. |
| `StorageAccounts_Get` | `EXEC` | `accountId, location, subscriptionId` | Returns the requested storage account. |
| `StorageAccounts_ReclaimStorageCapacity` | `EXEC` | `location, subscriptionId` | Start reclaim storage capacity on deleted storage objects. |
| `StorageAccounts_Undelete` | `EXEC` | `accountId, location, subscriptionId` | Undelete a deleted storage account with new account name if the a new name is provided. |
