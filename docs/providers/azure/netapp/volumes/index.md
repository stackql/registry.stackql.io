---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
  - netapp
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
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.netapp.volumes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `volumeType` | `string` | What type of volume is this. For destination volumes in Cross Region Replication, set type to DataProtection |
| `isDefaultQuotaEnabled` | `boolean` | Specifies if default quota is enabled for the volume. |
| `networkFeatures` | `string` | Basic network, or Standard features available to the volume. |
| `t2Network` | `string` | T2 network information |
| `volumeGroupName` | `string` | Volume Group Name |
| `ldapEnabled` | `boolean` | Specifies whether LDAP is enabled or not for a given NFS volume. |
| `encrypted` | `boolean` | Specifies if the volume is encrypted or not. Only available on volumes created or updated after 2022-01-01. |
| `maximumNumberOfFiles` | `integer` | Maximum number of files allowed. Needs a service request in order to be changed. Only allowed to be changed if volume quota is more than 4TiB. |
| `keyVaultPrivateEndpointResourceId` | `string` | The resource ID of private endpoint for KeyVault. It must reside in the same VNET as the volume. Only applicable if encryptionKeySource = 'Microsoft.KeyVault'. |
| `provisioningState` | `string` | Azure lifecycle management |
| `dataProtection` | `` | DataProtection type volumes include an object containing details of the replication |
| `volumeSpecName` | `string` | Volume spec name is the application specific designation or identifier for the particular volume in a volume group for e.g. data, log |
| `defaultUserQuotaInKiBs` | `integer` | Default user quota for volume in KiBs. If isDefaultQuotaEnabled is set, the minimum value of 4 KiBs applies . |
| `avsDataStore` | `string` | Specifies whether the volume is enabled for Azure VMware Solution (AVS) datastore purpose |
| `snapshotId` | `string` | UUID v4 or resource identifier used to identify the Snapshot. |
| `proximityPlacementGroup` | `string` | Proximity placement group associated with the volume |
| `encryptionKeySource` | `string` | Source of key used to encrypt data in volume. Applicable if NetApp account has encryption.keySource = 'Microsoft.KeyVault'. Possible values (case-insensitive) are: 'Microsoft.NetApp, Microsoft.KeyVault' |
| `smbContinuouslyAvailable` | `boolean` | Enables continuously available share property for smb volume. Only applicable for SMB volume |
| `baremetalTenantId` | `string` | Unique Baremetal Tenant Identifier. |
| `throughputMibps` | `number` |  |
| `securityStyle` | `string` | The security style of volume, default unix, defaults to ntfs for dual protocol or CIFS protocol |
| `tags` | `object` | Resource tags. |
| `protocolTypes` | `array` | Set of protocol types, default NFSv3, CIFS for SMB protocol |
| `storageToNetworkProximity` | `string` | Provides storage to network proximity information for the volume. |
| `defaultGroupQuotaInKiBs` | `integer` | Default group quota for volume in KiBs. If isDefaultQuotaEnabled is set, the minimum value of 4 KiBs applies. |
| `isRestoring` | `boolean` | Restoring |
| `usageThreshold` | `integer` | Maximum storage quota allowed for a file system in bytes. This is a soft quota used for alerting only. Minimum size is 100 GiB. Upper limit is 100TiB. Specified in bytes. |
| `subnetId` | `string` | The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `backupId` | `string` | UUID v4 or resource identifier used to identify the Backup. |
| `unixPermissions` | `string` | UNIX permissions for NFS volume accepted in octal 4 digit format. First digit selects the set user ID(4), set group ID (2) and sticky (1) attributes. Second digit selects permission for the owner of the file: read (4), write (2) and execute (1). Third selects permissions for other users in the same group. the fourth for other users not in the group. 0755 - gives read/write/execute permissions to owner and read/execute to group and other users. |
| `smbEncryption` | `boolean` | Enables encryption for in-flight smb3 data. Only applicable for SMB/DualProtocol volume. To be used with swagger version 2020-08-01 or later |
| `networkSiblingSetId` | `string` | Network Sibling Set ID for the the group of volumes sharing networking resources. |
| `zones` | `array` | Availability Zone |
| `creationToken` | `string` | A unique file path for the volume. Used when creating mount targets |
| `enableSubvolumes` | `string` | Flag indicating whether subvolume operations are enabled on the volume |
| `coolAccess` | `boolean` | Specifies whether Cool Access(tiering) is enabled for the volume. |
| `fileSystemId` | `string` | Unique FileSystem Identifier. |
| `cloneProgress` | `integer` | When a volume is being restored from another volume's snapshot, will show the percentage completion of this cloning process. When this value is empty/null there is no cloning process currently happening on this volume. This value will update every 5 minutes during cloning. |
| `serviceLevel` | `string` | The service level of the file system |
| `capacityPoolResourceId` | `string` | Pool Resource Id used in case of creating a volume through volume group |
| `snapshotDirectoryVisible` | `boolean` | If enabled (true) the volume will contain a read-only snapshot directory which provides access to each of the volume's snapshots (default to true). |
| `exportPolicy` | `` | Set of export policy rules |
| `kerberosEnabled` | `boolean` | Describe if a volume is KerberosEnabled. To be use with swagger version 2020-05-01 or later |
| `placementRules` | `array` | Application specific placement rules for the particular volume |
| `mountTargets` | `array` | List of mount targets |
| `location` | `string` | The geo-location where the resource lives |
| `coolnessPeriod` | `integer` | Specifies the number of days after which data that is not accessed by clients will be tiered. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Volumes_List` | `SELECT` | `accountName, poolName, resourceGroupName, subscriptionId` | List all volumes within the capacity pool |
| `Volumes_CreateOrUpdate` | `INSERT` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName, data__location` | Create or update the specified volume within the capacity pool |
| `Volumes_Delete` | `DELETE` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Delete the specified volume |
| `Volumes_AuthorizeReplication` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Authorize the replication connection on the source volume |
| `Volumes_BreakReplication` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Break the replication connection on the destination volume |
| `Volumes_DeleteReplication` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Delete the replication connection on the destination volume, and send release to the source replication |
| `Volumes_FinalizeRelocation` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Finalizes the relocation of the volume and cleans up the old volume. |
| `Volumes_Get` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Get the details of the specified volume |
| `Volumes_ListReplications` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | List all replications for a specified volume |
| `Volumes_PoolChange` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName, data__newPoolResourceId` | Moves volume to another pool |
| `Volumes_ReInitializeReplication` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Re-Initializes the replication connection on the destination volume |
| `Volumes_ReestablishReplication` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Re-establish a previously deleted replication between 2 volumes that have a common ad-hoc or policy-based snapshots |
| `Volumes_Relocate` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Relocates volume to a new stamp |
| `Volumes_ReplicationStatus` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Get the status of the replication |
| `Volumes_ResetCifsPassword` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Reset cifs password from volume |
| `Volumes_ResyncReplication` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Resync the connection on the destination volume. If the operation is ran on the source volume it will reverse-resync the connection and sync from destination to source. |
| `Volumes_Revert` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Revert a volume to the snapshot specified in the body |
| `Volumes_RevertRelocation` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Reverts the volume relocation process, cleans up the new volume and starts using the former-existing volume. |
| `Volumes_Update` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Patch the specified volume |
