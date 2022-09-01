---
title: file_shares
hide_title: false
hide_table_of_contents: false
keywords:
  - file_shares
  - storage
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
<tr><td><b>Name</b></td><td><code>file_shares</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage.file_shares</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `signedIdentifiers` | `array` | List of stored access policies specified on the share. |
| `deletedTime` | `string` | The deleted time if the share was deleted. |
| `remainingRetentionDays` | `integer` | Remaining retention days for share that was soft deleted. |
| `accessTier` | `string` | Access tier for specific share. GpV2 account can choose between TransactionOptimized (default), Hot, and Cool. FileStorage account can choose Premium. |
| `shareUsageBytes` | `integer` | The approximate size of the data stored on the share. Note that this value may not include all recently created or recently resized files. |
| `snapshotTime` | `string` | Creation time of share snapshot returned in the response of list shares with expand param "snapshots". |
| `shareQuota` | `integer` | The maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5TB (5120). For Large File Shares, the maximum size is 102400. |
| `lastModifiedTime` | `string` | Returns the date and time the share was last modified. |
| `accessTierChangeTime` | `string` | Indicates the last modification time for share access tier. |
| `leaseDuration` | `string` | Specifies whether the lease on a share is of infinite or fixed duration, only when the share is leased. |
| `deleted` | `boolean` | Indicates whether the share was deleted. |
| `metadata` | `object` | A name-value pair to associate with the share as metadata. |
| `leaseStatus` | `string` | The lease status of the share. |
| `enabledProtocols` | `string` | The authentication protocol that is used for the file share. Can only be specified when creating a share. |
| `leaseState` | `string` | Lease state of the share. |
| `etag` | `string` | Resource Etag. |
| `rootSquash` | `string` | The property is for NFS share only. The default is NoRootSquash. |
| `accessTierStatus` | `string` | Indicates if there is a pending transition for access tier. |
| `version` | `string` | The version of the share. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `FileShares_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Lists all shares. |
| `FileShares_Create` | `INSERT` | `accountName, resourceGroupName, shareName, subscriptionId` | Creates a new share under the specified account as described by request body. The share resource includes metadata and properties for that share. It does not include a list of the files contained by the share.  |
| `FileShares_Delete` | `DELETE` | `accountName, resourceGroupName, shareName, subscriptionId` | Deletes specified share under its account. |
| `FileShares_Get` | `EXEC` | `accountName, resourceGroupName, shareName, subscriptionId` | Gets properties of a specified share. |
| `FileShares_Lease` | `EXEC` | `accountName, resourceGroupName, shareName, subscriptionId, data__action` | The Lease Share operation establishes and manages a lock on a share for delete operations. The lock duration can be 15 to 60 seconds, or can be infinite. |
| `FileShares_Restore` | `EXEC` | `accountName, resourceGroupName, shareName, subscriptionId, data__deletedShareName, data__deletedShareVersion` | Restore a file share within a valid retention days if share soft delete is enabled |
| `FileShares_Update` | `EXEC` | `accountName, resourceGroupName, shareName, subscriptionId` | Updates share properties as specified in request body. Properties not mentioned in the request will not be changed. Update fails if the specified share does not already exist.  |
