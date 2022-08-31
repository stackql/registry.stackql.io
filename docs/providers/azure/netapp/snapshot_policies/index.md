---
title: snapshot_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshot_policies
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
<tr><td><b>Name</b></td><td><code>snapshot_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.netapp.snapshot_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `dailySchedule` | `object` | Daily Schedule properties |
| `monthlySchedule` | `object` | Monthly Schedule properties |
| `enabled` | `boolean` | The property to decide policy is enabled or not |
| `weeklySchedule` | `object` | Weekly Schedule properties, make a snapshot every week at a specific day or days |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `provisioningState` | `string` | Azure lifecycle management |
| `tags` | `object` | Resource tags. |
| `hourlySchedule` | `object` | Hourly Schedule properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SnapshotPolicies_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | List snapshot policy |
| `SnapshotPolicies_Create` | `INSERT` | `accountName, resourceGroupName, snapshotPolicyName, subscriptionId, data__location` | Create a snapshot policy |
| `SnapshotPolicies_Delete` | `DELETE` | `accountName, resourceGroupName, snapshotPolicyName, subscriptionId` | Delete snapshot policy |
| `SnapshotPolicies_Get` | `EXEC` | `accountName, resourceGroupName, snapshotPolicyName, subscriptionId` | Get a snapshot Policy |
| `SnapshotPolicies_ListVolumes` | `EXEC` | `accountName, resourceGroupName, snapshotPolicyName, subscriptionId` | Get volumes associated with snapshot policy |
| `SnapshotPolicies_Update` | `EXEC` | `accountName, resourceGroupName, snapshotPolicyName, subscriptionId` | Patch a snapshot policy |
