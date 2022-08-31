---
title: disk_restore_point
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_restore_point
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
<tr><td><b>Name</b></td><td><code>disk_restore_point</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.disk_restore_point</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `securityProfile` | `object` | Contains the security related information for the resource. |
| `osType` | `string` | The Operating System type. |
| `sourceUniqueId` | `string` | unique incarnation id of the source disk |
| `supportedCapabilities` | `object` | List of supported capabilities persisted on the disk resource for VM use. |
| `type` | `string` | Resource type |
| `hyperVGeneration` | `string` | The hypervisor generation of the Virtual Machine. Applicable to OS disks only. |
| `timeCreated` | `string` | The timestamp of restorePoint creation |
| `encryption` | `object` | Encryption at rest settings for disk or snapshot |
| `familyId` | `string` | id of the backing snapshot's MIS family |
| `completionPercent` | `number` | Percentage complete for the background copy of disk restore point when source resource is from a different region. |
| `diskAccessId` | `string` | ARM id of the DiskAccess resource for using private endpoints on disks. |
| `publicNetworkAccess` | `string` | Policy for controlling export on the disk. |
| `purchasePlan` | `object` | Used for establishing the purchase context of any 3rd Party artifact through MarketPlace. |
| `replicationState` | `string` | Replication state of disk restore point when source resource is from a different region. |
| `supportsHibernation` | `boolean` | Indicates the OS on a disk supports hibernation. |
| `sourceResourceLocation` | `string` | Location of source disk or source disk restore point when source resource is from a different region. |
| `networkAccessPolicy` | `string` | Policy for accessing the disk via network. |
| `sourceResourceId` | `string` | arm id of source disk or source disk restore point. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DiskRestorePoint_ListByRestorePoint` | `SELECT` | `resourceGroupName, restorePointCollectionName, subscriptionId, vmRestorePointName` | Lists diskRestorePoints under a vmRestorePoint. |
| `DiskRestorePoint_Get` | `EXEC` | `diskRestorePointName, resourceGroupName, restorePointCollectionName, subscriptionId, vmRestorePointName` | Get disk restorePoint resource |
| `DiskRestorePoint_GrantAccess` | `EXEC` | `diskRestorePointName, resourceGroupName, restorePointCollectionName, subscriptionId, vmRestorePointName, data__access, data__durationInSeconds` | Grants access to a diskRestorePoint. |
| `DiskRestorePoint_RevokeAccess` | `EXEC` | `diskRestorePointName, resourceGroupName, restorePointCollectionName, subscriptionId, vmRestorePointName` | Revokes access to a diskRestorePoint. |
