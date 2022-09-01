---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
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
<tr><td><b>Name</b></td><td><code>virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.system_center_vm_manager.virtual_machines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `type` | `string` | Resource Type |
| `location` | `string` | Gets or sets the location. |
| `checkpointType` | `string` | Type of checkpoint supported for the vm. |
| `tags` | `object` | Resource tags |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `inventoryItemId` | `string` | Gets or sets the inventory Item ID for the resource. |
| `vmmServerId` | `string` | ARM Id of the vmmServer resource in which this resource resides. |
| `generation` | `integer` | Gets or sets the generation for the vm. |
| `checkpoints` | `array` | Checkpoints in the vm. |
| `provisioningState` | `string` | Gets or sets the provisioning state. |
| `cloudId` | `string` | ARM Id of the cloud resource to use for deploying the vm. |
| `extendedLocation` | `object` | The extended location. |
| `powerState` | `string` | Gets the power state of the virtual machine. |
| `networkProfile` | `object` | Defines the resource properties. |
| `storageProfile` | `object` | Defines the resource properties. |
| `hardwareProfile` | `object` | Defines the resource properties. |
| `templateId` | `string` | ARM Id of the template resource to use for deploying the vm. |
| `vmName` | `string` | VMName is the name of VM on the SCVMM server. |
| `availabilitySets` | `array` | Availability Sets in vm. |
| `uuid` | `string` | Unique ID of the virtual machine. |
| `osProfile` | `object` | Defines the resource properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachines_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List of VirtualMachines in a resource group. |
| `VirtualMachines_ListBySubscription` | `SELECT` | `subscriptionId` | List of VirtualMachines in a subscription. |
| `VirtualMachines_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, virtualMachineName, data__extendedLocation, data__location` | Creates Or Updates virtual machines deployed on scvmm fabric. |
| `VirtualMachines_Delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualMachineName` | Deletes a VirtualMachine deployed on ScVmm fabric. |
| `VirtualMachines_CreateCheckpoint` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineName` | Creates a checkpoint in virtual machine. |
| `VirtualMachines_DeleteCheckpoint` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineName` | Deletes a checkpoint in virtual machine. |
| `VirtualMachines_Get` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineName` | Implements VirtualMachine GET method. |
| `VirtualMachines_Restart` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineName` | Restart virtual machine. |
| `VirtualMachines_RestoreCheckpoint` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineName` | Restores to a checkpoint in virtual machine. |
| `VirtualMachines_Start` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineName` | Start virtual machine. |
| `VirtualMachines_Stop` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineName` | Stop virtual machine. |
| `VirtualMachines_Update` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineName` | Updates the VirtualMachines resource. |
