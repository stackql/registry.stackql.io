---
title: disks
hide_title: false
hide_table_of_contents: false
keywords:
  - disks
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
<tr><td><b>Name</b></td><td><code>disks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.disks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `extendedLocation` | `object` | The complex type of the extended location. |
| `hyperVGeneration` | `string` | The hypervisor generation of the Virtual Machine. Applicable to OS disks only. |
| `supportsHibernation` | `boolean` | Indicates the OS on a disk supports hibernation. |
| `diskSizeGB` | `integer` | If creationData.createOption is Empty, this field is mandatory and it indicates the size of the disk to create. If this field is present for updates or creation with other options, it indicates a resize. Resizes are only allowed if the disk is not attached to a running VM, and can only increase the disk's size. |
| `managedByExtended` | `array` | List of relative URIs containing the IDs of the VMs that have the disk attached. maxShares should be set to a value greater than one for disks to allow attaching them to multiple VMs. |
| `networkAccessPolicy` | `string` | Policy for accessing the disk via network. |
| `tags` | `object` | Resource tags |
| `purchasePlan` | `object` | Used for establishing the purchase context of any 3rd Party artifact through MarketPlace. |
| `diskMBpsReadOnly` | `integer` | The total throughput (MBps) that will be allowed across all VMs mounting the shared disk as ReadOnly. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10. |
| `diskMBpsReadWrite` | `integer` | The bandwidth allowed for this disk; only settable for UltraSSD disks. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10. |
| `uniqueId` | `string` | Unique Guid identifying the resource. |
| `zones` | `array` | The Logical zone list for Disk. |
| `location` | `string` | Resource location |
| `propertyUpdatesInProgress` | `object` | Properties of the disk for which update is pending. |
| `maxShares` | `integer` | The maximum number of VMs that can attach to the disk at the same time. Value greater than one indicates a disk that can be mounted on multiple VMs at the same time. |
| `sku` | `object` | The disks sku name. Can be Standard_LRS, Premium_LRS, StandardSSD_LRS, UltraSSD_LRS, Premium_ZRS, StandardSSD_ZRS, or PremiumV2_LRS. |
| `encryption` | `object` | Encryption at rest settings for disk or snapshot |
| `burstingEnabled` | `boolean` | Set to true to enable bursting beyond the provisioned performance target of the disk. Bursting is disabled by default. Does not apply to Ultra disks. |
| `provisioningState` | `string` | The disk provisioning state. |
| `dataAccessAuthMode` | `string` | Additional authentication requirements when exporting or uploading to a disk or snapshot. |
| `securityProfile` | `object` | Contains the security related information for the resource. |
| `shareInfo` | `array` | Details of the list of all VMs that have the disk attached. maxShares should be set to a value greater than one for disks to allow attaching them to multiple VMs. |
| `diskState` | `string` | This enumerates the possible state of the disk. |
| `type` | `string` | Resource type |
| `supportedCapabilities` | `object` | List of supported capabilities persisted on the disk resource for VM use. |
| `completionPercent` | `number` | Percentage complete for the background copy when a resource is created via the CopyStart operation. |
| `diskAccessId` | `string` | ARM id of the DiskAccess resource for using private endpoints on disks. |
| `tier` | `string` | Performance tier of the disk (e.g, P4, S10) as described here: https://azure.microsoft.com/en-us/pricing/details/managed-disks/. Does not apply to Ultra disks. |
| `creationData` | `object` | Data used when creating a disk. |
| `encryptionSettingsCollection` | `object` | Encryption settings for disk or snapshot |
| `diskIOPSReadWrite` | `integer` | The number of IOPS allowed for this disk; only settable for UltraSSD disks. One operation can transfer between 4k and 256k bytes. |
| `osType` | `string` | The Operating System type. |
| `publicNetworkAccess` | `string` | Policy for controlling export on the disk. |
| `timeCreated` | `string` | The time when the disk was created. |
| `diskSizeBytes` | `integer` | The size of the disk in bytes. This field is read only. |
| `managedBy` | `string` | A relative URI containing the ID of the VM that has the disk attached. |
| `diskIOPSReadOnly` | `integer` | The total number of IOPS that will be allowed across all VMs mounting the shared disk as ReadOnly. One operation can transfer between 4k and 256k bytes. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Disks_List` | `SELECT` | `subscriptionId` | Lists all the disks under a subscription. |
| `Disks_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the disks under a resource group. |
| `Disks_CreateOrUpdate` | `INSERT` | `diskName, resourceGroupName, subscriptionId` | Creates or updates a disk. |
| `Disks_Delete` | `DELETE` | `diskName, resourceGroupName, subscriptionId` | Deletes a disk. |
| `Disks_Get` | `EXEC` | `diskName, resourceGroupName, subscriptionId` | Gets information about a disk. |
| `Disks_GrantAccess` | `EXEC` | `diskName, resourceGroupName, subscriptionId, data__access, data__durationInSeconds` | Grants access to a disk. |
| `Disks_RevokeAccess` | `EXEC` | `diskName, resourceGroupName, subscriptionId` | Revokes access to a disk. |
| `Disks_Update` | `EXEC` | `diskName, resourceGroupName, subscriptionId` | Updates (patches) a disk. |
