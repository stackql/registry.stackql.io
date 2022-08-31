---
title: clouds
hide_title: false
hide_table_of_contents: false
keywords:
  - clouds
  - system_center_vm_manager
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
<tr><td><b>Name</b></td><td><code>clouds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.system_center_vm_manager.clouds</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `tags` | `object` | Resource tags |
| `inventoryItemId` | `string` | Gets or sets the inventory Item ID for the resource. |
| `location` | `string` | Gets or sets the location. |
| `storageQoSPolicies` | `array` | List of QoS policies available for the cloud. |
| `uuid` | `string` | Unique ID of the cloud. |
| `cloudName` | `string` | Name of the cloud in VMMServer. |
| `type` | `string` | Resource Type |
| `vmmServerId` | `string` | ARM Id of the vmmServer resource in which this resource resides. |
| `provisioningState` | `string` | Gets or sets the provisioning state. |
| `extendedLocation` | `object` | The extended location. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `cloudCapacity` | `object` | Cloud Capacity model |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Clouds_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List of Clouds in a resource group. |
| `Clouds_ListBySubscription` | `SELECT` | `subscriptionId` | List of Clouds in a subscription. |
| `Clouds_CreateOrUpdate` | `INSERT` | `cloudName, resourceGroupName, subscriptionId, data__extendedLocation, data__location` | Onboards the ScVmm fabric cloud as an Azure cloud resource. |
| `Clouds_Delete` | `DELETE` | `cloudName, resourceGroupName, subscriptionId` | Deregisters the ScVmm fabric cloud from Azure. |
| `Clouds_Get` | `EXEC` | `cloudName, resourceGroupName, subscriptionId` | Implements Cloud GET method. |
| `Clouds_Update` | `EXEC` | `cloudName, resourceGroupName, subscriptionId` | Updates the Clouds resource. |
