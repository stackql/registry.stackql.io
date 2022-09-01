---
title: iscsi_targets
hide_title: false
hide_table_of_contents: false
keywords:
  - iscsi_targets
  - storage_pool
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
<tr><td><b>Name</b></td><td><code>iscsi_targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_pool.iscsi_targets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `status` | `string` | Operational status of the resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `endpoints` | `array` | List of private IPv4 addresses to connect to the iSCSI Target. |
| `provisioningState` | `string` | Provisioning state of the iSCSI Target. |
| `managedBy` | `string` | Azure resource id. Indicates if this resource is managed by another Azure resource. |
| `sessions` | `array` | List of identifiers for active sessions on the iSCSI target |
| `targetIqn` | `string` | iSCSI Target IQN (iSCSI Qualified Name); example: "iqn.2005-03.org.iscsi:server". |
| `port` | `integer` | The port used by iSCSI Target portal group. |
| `luns` | `array` | List of LUNs to be exposed through iSCSI Target. |
| `managedByExtended` | `array` | List of Azure resource ids that manage this resource. |
| `aclMode` | `string` | ACL mode for iSCSI Target. |
| `staticAcls` | `array` | Access Control List (ACL) for an iSCSI Target; defines LUN masking policy |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IscsiTargets_ListByDiskPool` | `SELECT` | `diskPoolName, resourceGroupName, subscriptionId` | Get iSCSI Targets in a Disk pool. |
| `IscsiTargets_CreateOrUpdate` | `INSERT` | `diskPoolName, iscsiTargetName, resourceGroupName, subscriptionId` | Create or Update an iSCSI Target. |
| `IscsiTargets_Delete` | `DELETE` | `diskPoolName, iscsiTargetName, resourceGroupName, subscriptionId` | Delete an iSCSI Target. |
| `IscsiTargets_Get` | `EXEC` | `diskPoolName, iscsiTargetName, resourceGroupName, subscriptionId` | Get an iSCSI Target. |
| `IscsiTargets_Update` | `EXEC` | `diskPoolName, iscsiTargetName, resourceGroupName, subscriptionId` | Update an iSCSI Target. |
