---
title: proximity_placement_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - proximity_placement_groups
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
<tr><td><b>Name</b></td><td><code>proximity_placement_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.proximity_placement_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `virtualMachines` | `array` | A list of references to all virtual machines in the proximity placement group. |
| `type` | `string` | Resource type |
| `tags` | `object` | Resource tags |
| `location` | `string` | Resource location |
| `proximityPlacementGroupType` | `string` | Specifies the type of the proximity placement group. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; **Standard** : Co-locate resources within an Azure region or Availability Zone. &lt;br&gt;&lt;br&gt; **Ultra** : For future use. |
| `colocationStatus` | `object` | Instance view status. |
| `availabilitySets` | `array` | A list of references to all availability sets in the proximity placement group. |
| `virtualMachineScaleSets` | `array` | A list of references to all virtual machine scale sets in the proximity placement group. |
| `zones` | `array` | Specifies the Availability Zone where virtual machine, virtual machine scale set or availability set associated with the  proximity placement group can be created. |
| `intent` | `object` | Specifies the user intent of the proximity placement group. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ProximityPlacementGroups_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all proximity placement groups in a resource group. |
| `ProximityPlacementGroups_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all proximity placement groups in a subscription. |
| `ProximityPlacementGroups_CreateOrUpdate` | `INSERT` | `proximityPlacementGroupName, resourceGroupName, subscriptionId` | Create or update a proximity placement group. |
| `ProximityPlacementGroups_Delete` | `DELETE` | `proximityPlacementGroupName, resourceGroupName, subscriptionId` | Delete a proximity placement group. |
| `ProximityPlacementGroups_Get` | `EXEC` | `proximityPlacementGroupName, resourceGroupName, subscriptionId` | Retrieves information about a proximity placement group . |
| `ProximityPlacementGroups_Update` | `EXEC` | `proximityPlacementGroupName, resourceGroupName, subscriptionId` | Update a proximity placement group. |
