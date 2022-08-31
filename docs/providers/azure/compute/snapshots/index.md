---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - compute
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
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.snapshots</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `incremental` | `boolean` | Whether a snapshot is incremental. Incremental snapshots on the same disk occupy less space than full snapshots and can be diffed. |
| `networkAccessPolicy` | `string` | Policy for accessing the disk via network. |
| `uniqueId` | `string` | Unique Guid identifying the resource. |
| `dataAccessAuthMode` | `string` | Additional authentication requirements when exporting or uploading to a disk or snapshot. |
| `securityProfile` | `object` | Contains the security related information for the resource. |
| `publicNetworkAccess` | `string` | Policy for controlling export on the disk. |
| `supportsHibernation` | `boolean` | Indicates the OS on a snapshot supports hibernation. |
| `hyperVGeneration` | `string` | The hypervisor generation of the Virtual Machine. Applicable to OS disks only. |
| `tags` | `object` | Resource tags |
| `creationData` | `object` | Data used when creating a disk. |
| `diskSizeGB` | `integer` | If creationData.createOption is Empty, this field is mandatory and it indicates the size of the disk to create. If this field is present for updates or creation with other options, it indicates a resize. Resizes are only allowed if the disk is not attached to a running VM, and can only increase the disk's size. |
| `encryptionSettingsCollection` | `object` | Encryption settings for disk or snapshot |
| `timeCreated` | `string` | The time when the snapshot was created. |
| `diskSizeBytes` | `integer` | The size of the disk in bytes. This field is read only. |
| `managedBy` | `string` | Unused. Always Null. |
| `location` | `string` | Resource location |
| `diskAccessId` | `string` | ARM id of the DiskAccess resource for using private endpoints on disks. |
| `osType` | `string` | The Operating System type. |
| `sku` | `object` | The snapshots sku name. Can be Standard_LRS, Premium_LRS, or Standard_ZRS. This is an optional parameter for incremental snapshot and the default behavior is the SKU will be set to the same sku as the previous snapshot |
| `purchasePlan` | `object` | Used for establishing the purchase context of any 3rd Party artifact through MarketPlace. |
| `encryption` | `object` | Encryption at rest settings for disk or snapshot |
| `completionPercent` | `number` | Percentage complete for the background copy when a resource is created via the CopyStart operation. |
| `supportedCapabilities` | `object` | List of supported capabilities persisted on the disk resource for VM use. |
| `extendedLocation` | `object` | The complex type of the extended location. |
| `copyCompletionError` | `object` | Indicates the error details if the background copy of a resource created via the CopyStart operation fails. |
| `provisioningState` | `string` | The disk provisioning state. |
| `type` | `string` | Resource type |
| `diskState` | `string` | This enumerates the possible state of the disk. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Snapshots_List` | `SELECT` | `subscriptionId` | Lists snapshots under a subscription. |
| `Snapshots_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists snapshots under a resource group. |
| `Snapshots_CreateOrUpdate` | `INSERT` | `resourceGroupName, snapshotName, subscriptionId` | Creates or updates a snapshot. |
| `Snapshots_Delete` | `DELETE` | `resourceGroupName, snapshotName, subscriptionId` | Deletes a snapshot. |
| `Snapshots_Get` | `EXEC` | `resourceGroupName, snapshotName, subscriptionId` | Gets information about a snapshot. |
| `Snapshots_GrantAccess` | `EXEC` | `resourceGroupName, snapshotName, subscriptionId, data__access, data__durationInSeconds` | Grants access to a snapshot. |
| `Snapshots_RevokeAccess` | `EXEC` | `resourceGroupName, snapshotName, subscriptionId` | Revokes access to a snapshot. |
| `Snapshots_Update` | `EXEC` | `resourceGroupName, snapshotName, subscriptionId` | Updates (patches) a snapshot. |
