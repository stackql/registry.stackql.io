---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - container_service
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
<tr><td><b>Id</b></td><td><code>azure.container_service.snapshots</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `creationData` | `object` | Data used when creating a target resource from a source resource. |
| `vmSize` | `string` | The size of the VM. |
| `osSku` | `string` | Specifies an OS SKU. This value must not be specified if OSType is Windows. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
| `snapshotType` | `string` | The type of a snapshot. The default is NodePool. |
| `nodeImageVersion` | `string` | The version of node image. |
| `osType` | `string` | The operating system type. The default is Linux. |
| `enableFIPS` | `boolean` | Whether to use a FIPS-enabled OS. |
| `kubernetesVersion` | `string` | The version of Kubernetes. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Snapshots_List` | `SELECT` | `subscriptionId` |
| `Snapshots_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` |
| `Snapshots_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` |
| `Snapshots_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` |
| `Snapshots_Get` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |
| `Snapshots_UpdateTags` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |
