---
title: virtual_machine_scale_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_sets
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
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machine_scale_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `plan` | `object` | Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started -&gt;**. Enter any required information and then click **Save**. |
| `zoneBalance` | `boolean` | Whether to force strictly even Virtual Machine distribution cross x-zones in case there is zone outage. zoneBalance property can only be set if the zones property of the scale set contains more than one zone. If there are no zones or only one zone specified, then zoneBalance property should not be set. |
| `identity` | `object` | Identity for the virtual machine scale set. |
| `hostGroup` | `object` |  |
| `virtualMachineProfile` | `object` | Describes a virtual machine scale set virtual machine profile. |
| `singlePlacementGroup` | `boolean` | When true this limits the scale set to a single placement group, of max size 100 virtual machines. NOTE: If singlePlacementGroup is true, it may be modified to false. However, if singlePlacementGroup is false, it may not be modified to true. |
| `spotRestorePolicy` | `object` | Specifies the Spot-Try-Restore properties for the virtual machine scale set. &lt;br&gt;&lt;br&gt; With this property customer can enable or disable automatic restore of the evicted Spot VMSS VM instances opportunistically based on capacity availability and pricing constraint. |
| `additionalCapabilities` | `object` | Enables or disables a capability on the virtual machine or virtual machine scale set. |
| `location` | `string` | Resource location |
| `provisioningState` | `string` | The provisioning state, which only appears in the response. |
| `orchestrationMode` | `string` | Specifies the orchestration mode for the virtual machine scale set. |
| `doNotRunExtensionsOnOverprovisionedVMs` | `boolean` | When Overprovision is enabled, extensions are launched only on the requested number of VMs which are finally kept. This property will hence ensure that the extensions do not run on the extra overprovisioned VMs. |
| `overprovision` | `boolean` | Specifies whether the Virtual Machine Scale Set should be overprovisioned. |
| `uniqueId` | `string` | Specifies the ID which uniquely identifies a Virtual Machine Scale Set. |
| `automaticRepairsPolicy` | `object` | Specifies the configuration parameters for automatic repairs on the virtual machine scale set. |
| `zones` | `array` | The virtual machine scale set zones. NOTE: Availability zones can only be set when you create the scale set |
| `sku` | `object` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |
| `type` | `string` | Resource type |
| `tags` | `object` | Resource tags |
| `upgradePolicy` | `object` | Describes an upgrade policy - automatic, manual, or rolling. |
| `platformFaultDomainCount` | `integer` | Fault Domain count for each placement group. |
| `scaleInPolicy` | `object` | Describes a scale-in policy for a virtual machine scale set. |
| `timeCreated` | `string` | Specifies the time at which the Virtual Machine Scale Set resource was created.&lt;br&gt;&lt;br&gt;Minimum api-version: 2022-03-01. |
| `proximityPlacementGroup` | `object` |  |
| `extendedLocation` | `object` | The complex type of the extended location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachineScaleSets_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of all VM scale sets under a resource group. |
| `VirtualMachineScaleSets_ListAll` | `SELECT` | `subscriptionId` | Gets a list of all VM Scale Sets in the subscription, regardless of the associated resource group. Use nextLink property in the response to get the next page of VM Scale Sets. Do this till nextLink is null to fetch all the VM Scale Sets. |
| `VirtualMachineScaleSets_ListByLocation` | `SELECT` | `location, subscriptionId` | Gets all the VM scale sets under the specified subscription for the specified location. |
| `VirtualMachineScaleSets_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, vmScaleSetName` | Create or update a VM scale set. |
| `VirtualMachineScaleSets_Delete` | `DELETE` | `resourceGroupName, subscriptionId, vmScaleSetName` | Deletes a VM scale set. |
| `VirtualMachineScaleSets_ConvertToSinglePlacementGroup` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Converts SinglePlacementGroup property to false for a existing virtual machine scale set. |
| `VirtualMachineScaleSets_Deallocate` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Deallocates specific virtual machines in a VM scale set. Shuts down the virtual machines and releases the compute resources. You are not billed for the compute resources that this virtual machine scale set deallocates. |
| `VirtualMachineScaleSets_DeleteInstances` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName, data__instanceIds` | Deletes virtual machines in a VM scale set. |
| `VirtualMachineScaleSets_ForceRecoveryServiceFabricPlatformUpdateDomainWalk` | `EXEC` | `platformUpdateDomain, resourceGroupName, subscriptionId, vmScaleSetName` | Manual platform update domain walk to update virtual machines in a service fabric virtual machine scale set. |
| `VirtualMachineScaleSets_Get` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Display information about a virtual machine scale set. |
| `VirtualMachineScaleSets_GetInstanceView` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Gets the status of a VM scale set instance. |
| `VirtualMachineScaleSets_GetOSUpgradeHistory` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Gets list of OS upgrades on a VM scale set instance. |
| `VirtualMachineScaleSets_ListSkus` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Gets a list of SKUs available for your VM scale set, including the minimum and maximum VM instances allowed for each SKU. |
| `VirtualMachineScaleSets_PerformMaintenance` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Perform maintenance on one or more virtual machines in a VM scale set. Operation on instances which are not eligible for perform maintenance will be failed. Please refer to best practices for more details: https://docs.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-maintenance-notifications |
| `VirtualMachineScaleSets_PowerOff` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Power off (stop) one or more virtual machines in a VM scale set. Note that resources are still attached and you are getting charged for the resources. Instead, use deallocate to release resources and avoid charges. |
| `VirtualMachineScaleSets_Redeploy` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Shuts down all the virtual machines in the virtual machine scale set, moves them to a new node, and powers them back on. |
| `VirtualMachineScaleSets_Reimage` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Reimages (upgrade the operating system) one or more virtual machines in a VM scale set which don't have a ephemeral OS disk, for virtual machines who have a ephemeral OS disk the virtual machine is reset to initial state. |
| `VirtualMachineScaleSets_ReimageAll` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Reimages all the disks ( including data disks ) in the virtual machines in a VM scale set. This operation is only supported for managed disks. |
| `VirtualMachineScaleSets_Restart` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Restarts one or more virtual machines in a VM scale set. |
| `VirtualMachineScaleSets_SetOrchestrationServiceState` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName, data__action, data__serviceName` | Changes ServiceState property for a given service |
| `VirtualMachineScaleSets_Start` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Starts one or more virtual machines in a VM scale set. |
| `VirtualMachineScaleSets_Update` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Update a VM scale set. |
| `VirtualMachineScaleSets_UpdateInstances` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName, data__instanceIds` | Upgrades one or more virtual machines to the latest SKU set in the VM scale set model. |
