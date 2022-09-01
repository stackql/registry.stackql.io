---
title: virtual_machine_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_templates
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
<tr><td><b>Name</b></td><td><code>virtual_machine_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.system_center_vm_manager.virtual_machine_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `provisioningState` | `string` | Gets or sets the provisioning state. |
| `generation` | `integer` | Gets or sets the generation for the vm. |
| `inventoryItemId` | `string` | Gets or sets the inventory Item ID for the resource. |
| `computerName` | `string` | Gets or sets computer name. |
| `isHighlyAvailable` | `string` | Gets highly available property. |
| `location` | `string` | Gets or sets the location. |
| `osType` | `string` | Defines the different types of VM guest operating systems. |
| `osName` | `string` | Gets or sets os name. |
| `dynamicMemoryMinMB` | `integer` | Gets or sets the min dynamic memory for the vm. |
| `type` | `string` | Resource Type |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `cpuCount` | `integer` | Gets or sets the desired number of vCPUs for the vm. |
| `dynamicMemoryMaxMB` | `integer` | Gets or sets the max dynamic memory for the vm. |
| `tags` | `object` | Resource tags |
| `dynamicMemoryEnabled` | `string` | Gets or sets a value indicating whether to enable dynamic memory or not. |
| `isCustomizable` | `string` | Gets or sets a value indicating whether the vm template is customizable or not. |
| `uuid` | `string` | Unique ID of the virtual machine template. |
| `disks` | `array` | Gets or sets the disks of the template. |
| `limitCpuForMigration` | `string` | Gets or sets a value indicating whether to enable processor compatibility mode for live migration of VMs. |
| `memoryMB` | `integer` | MemoryMB is the desired size of a virtual machine's memory, in MB. |
| `vmmServerId` | `string` | ARM Id of the vmmServer resource in which this resource resides. |
| `networkInterfaces` | `array` | Gets or sets the network interfaces of the template. |
| `extendedLocation` | `object` | The extended location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachineTemplates_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List of VirtualMachineTemplates in a resource group. |
| `VirtualMachineTemplates_ListBySubscription` | `SELECT` | `subscriptionId` | List of VirtualMachineTemplates in a subscription. |
| `VirtualMachineTemplates_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, virtualMachineTemplateName, data__extendedLocation, data__location` | Onboards the ScVmm VM Template as an Azure VM Template resource. |
| `VirtualMachineTemplates_Delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualMachineTemplateName` | Deregisters the ScVmm VM Template from Azure. |
| `VirtualMachineTemplates_Get` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineTemplateName` | Implements VirtualMachineTemplate GET method. |
| `VirtualMachineTemplates_Update` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineTemplateName` | Updates the VirtualMachineTemplate resource. |
