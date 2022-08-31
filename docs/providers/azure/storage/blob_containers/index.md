---
title: blob_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - blob_containers
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
<tr><td><b>Name</b></td><td><code>blob_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage.blob_containers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `enableNfsV3RootSquash` | `boolean` | Enable NFSv3 root squash on blob container. |
| `publicAccess` | `string` | Specifies whether data in the container may be accessed publicly and the level of access. |
| `remainingRetentionDays` | `integer` | Remaining retention days for soft deleted blob container. |
| `hasImmutabilityPolicy` | `boolean` | The hasImmutabilityPolicy public property is set to true by SRP if ImmutabilityPolicy has been created for this container. The hasImmutabilityPolicy public property is set to false by SRP if ImmutabilityPolicy has not been created for this container. |
| `hasLegalHold` | `boolean` | The hasLegalHold public property is set to true by SRP if there are at least one existing tag. The hasLegalHold public property is set to false by SRP if all existing legal hold tags are cleared out. There can be a maximum of 1000 blob containers with hasLegalHold=true for a given account. |
| `leaseDuration` | `string` | Specifies whether the lease on a container is of infinite or fixed duration, only when the container is leased. |
| `leaseStatus` | `string` | The lease status of the container. |
| `deleted` | `boolean` | Indicates whether the blob container was deleted. |
| `enableNfsV3AllSquash` | `boolean` | Enable NFSv3 all squash on blob container. |
| `etag` | `string` | Resource Etag. |
| `denyEncryptionScopeOverride` | `boolean` | Block override of encryption scope from the container default. |
| `immutabilityPolicy` | `object` | The properties of an ImmutabilityPolicy of a blob container. |
| `lastModifiedTime` | `string` | Returns the date and time the container was last modified. |
| `immutableStorageWithVersioning` | `object` | Object level immutability properties of the container. |
| `version` | `string` | The version of the deleted blob container. |
| `deletedTime` | `string` | Blob container deletion time. |
| `leaseState` | `string` | Lease state of the container. |
| `defaultEncryptionScope` | `string` | Default the container to use specified encryption scope for all writes. |
| `legalHold` | `object` | The LegalHold property of a blob container. |
| `metadata` | `object` | A name-value pair to associate with the container as metadata. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BlobContainers_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Lists all containers and does not support a prefix like data plane. Also SRP today does not return continuation token. |
| `BlobContainers_Create` | `INSERT` | `accountName, containerName, resourceGroupName, subscriptionId` | Creates a new container under the specified account as described by request body. The container resource includes metadata and properties for that container. It does not include a list of the blobs contained by the container.  |
| `BlobContainers_Delete` | `DELETE` | `accountName, containerName, resourceGroupName, subscriptionId` | Deletes specified container under its account. |
| `BlobContainers_ClearLegalHold` | `EXEC` | `accountName, containerName, resourceGroupName, subscriptionId, data__tags` | Clears legal hold tags. Clearing the same or non-existent tag results in an idempotent operation. ClearLegalHold clears out only the specified tags in the request. |
| `BlobContainers_CreateOrUpdateImmutabilityPolicy` | `EXEC` | `accountName, containerName, immutabilityPolicyName, resourceGroupName, subscriptionId` | Creates or updates an unlocked immutability policy. ETag in If-Match is honored if given but not required for this operation. |
| `BlobContainers_DeleteImmutabilityPolicy` | `EXEC` | `If-Match, accountName, containerName, immutabilityPolicyName, resourceGroupName, subscriptionId` | Aborts an unlocked immutability policy. The response of delete has immutabilityPeriodSinceCreationInDays set to 0. ETag in If-Match is required for this operation. Deleting a locked immutability policy is not allowed, the only way is to delete the container after deleting all expired blobs inside the policy locked container. |
| `BlobContainers_ExtendImmutabilityPolicy` | `EXEC` | `If-Match, accountName, containerName, resourceGroupName, subscriptionId` | Extends the immutabilityPeriodSinceCreationInDays of a locked immutabilityPolicy. The only action allowed on a Locked policy will be this action. ETag in If-Match is required for this operation. |
| `BlobContainers_Get` | `EXEC` | `accountName, containerName, resourceGroupName, subscriptionId` | Gets properties of a specified container.  |
| `BlobContainers_GetImmutabilityPolicy` | `EXEC` | `accountName, containerName, immutabilityPolicyName, resourceGroupName, subscriptionId` | Gets the existing immutability policy along with the corresponding ETag in response headers and body. |
| `BlobContainers_Lease` | `EXEC` | `accountName, containerName, resourceGroupName, subscriptionId, data__action` | The Lease Container operation establishes and manages a lock on a container for delete operations. The lock duration can be 15 to 60 seconds, or can be infinite. |
| `BlobContainers_LockImmutabilityPolicy` | `EXEC` | `If-Match, accountName, containerName, resourceGroupName, subscriptionId` | Sets the ImmutabilityPolicy to Locked state. The only action allowed on a Locked policy is ExtendImmutabilityPolicy action. ETag in If-Match is required for this operation. |
| `BlobContainers_ObjectLevelWorm` | `EXEC` | `accountName, containerName, resourceGroupName, subscriptionId` | This operation migrates a blob container from container level WORM to object level immutability enabled container. Prerequisites require a container level immutability policy either in locked or unlocked state, Account level versioning must be enabled and there should be no Legal hold on the container. |
| `BlobContainers_SetLegalHold` | `EXEC` | `accountName, containerName, resourceGroupName, subscriptionId, data__tags` | Sets legal hold tags. Setting the same tag results in an idempotent operation. SetLegalHold follows an append pattern and does not clear out the existing tags that are not specified in the request. |
| `BlobContainers_Update` | `EXEC` | `accountName, containerName, resourceGroupName, subscriptionId` | Updates container properties as specified in request body. Properties not mentioned in the request will be unchanged. Update fails if the specified container doesn't already exist.  |
