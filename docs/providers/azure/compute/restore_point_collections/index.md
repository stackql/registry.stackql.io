---
title: restore_point_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - restore_point_collections
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
<tr><td><b>Name</b></td><td><code>restore_point_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.restore_point_collections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `location` | `string` | Resource location |
| `restorePoints` | `array` | A list containing all restore points created under this restore point collection. |
| `provisioningState` | `string` | The provisioning state of the restore point collection. |
| `restorePointCollectionId` | `string` | The unique id of the restore point collection. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
| `source` | `object` | The properties of the source resource that this restore point collection is created from. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RestorePointCollections_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets the list of restore point collections in a resource group. |
| `RestorePointCollections_ListAll` | `SELECT` | `subscriptionId` | Gets the list of restore point collections in the subscription. Use nextLink property in the response to get the next page of restore point collections. Do this till nextLink is not null to fetch all the restore point collections. |
| `RestorePointCollections_CreateOrUpdate` | `INSERT` | `resourceGroupName, restorePointCollectionName, subscriptionId` | The operation to create or update the restore point collection. Please refer to https://aka.ms/RestorePoints for more details. When updating a restore point collection, only tags may be modified. |
| `RestorePointCollections_Delete` | `DELETE` | `resourceGroupName, restorePointCollectionName, subscriptionId` | The operation to delete the restore point collection. This operation will also delete all the contained restore points. |
| `RestorePointCollections_Get` | `EXEC` | `resourceGroupName, restorePointCollectionName, subscriptionId` | The operation to get the restore point collection. |
| `RestorePointCollections_Update` | `EXEC` | `resourceGroupName, restorePointCollectionName, subscriptionId` | The operation to update the restore point collection. |
