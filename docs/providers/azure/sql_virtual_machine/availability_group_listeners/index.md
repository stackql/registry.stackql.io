---
title: availability_group_listeners
hide_title: false
hide_table_of_contents: false
keywords:
  - availability_group_listeners
  - sql_virtual_machine
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
<tr><td><b>Name</b></td><td><code>availability_group_listeners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql_virtual_machine.availability_group_listeners</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `createDefaultAvailabilityGroupIfNotExist` | `boolean` | Create a default availability group if it does not exist. |
| `loadBalancerConfigurations` | `array` | List of load balancer configurations for an availability group listener. |
| `multiSubnetIpConfigurations` | `array` | List of multi subnet IP configurations for an AG listener. |
| `port` | `integer` | Listener port. |
| `provisioningState` | `string` | Provisioning state to track the async operation status. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `availabilityGroupConfiguration` | `object` | Availability group configuration. |
| `availabilityGroupName` | `string` | Name of the availability group. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AvailabilityGroupListeners_ListByGroup` | `SELECT` | `resourceGroupName, sqlVirtualMachineGroupName, subscriptionId` | Lists all availability group listeners in a SQL virtual machine group. |
| `AvailabilityGroupListeners_CreateOrUpdate` | `INSERT` | `availabilityGroupListenerName, resourceGroupName, sqlVirtualMachineGroupName, subscriptionId` | Creates or updates an availability group listener. |
| `AvailabilityGroupListeners_Delete` | `DELETE` | `availabilityGroupListenerName, resourceGroupName, sqlVirtualMachineGroupName, subscriptionId` | Deletes an availability group listener. |
| `AvailabilityGroupListeners_Get` | `EXEC` | `availabilityGroupListenerName, resourceGroupName, sqlVirtualMachineGroupName, subscriptionId` | Gets an availability group listener. |
