---
title: virtual_machine_scale_set_vms
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_set_vms
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
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_set_vms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machine_scale_set_vms</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `networkProfile` | `object` | Specifies the network interfaces or the networking configuration of the virtual machine. |
| `modelDefinitionApplied` | `string` | Specifies whether the model applied to the virtual machine is the model of the virtual machine scale set or the customized model for the virtual machine. |
| `zones` | `array` | The virtual machine zones. |
| `storageProfile` | `object` | Specifies the storage settings for the virtual machine disks. |
| `provisioningState` | `string` | The provisioning state, which only appears in the response. |
| `licenseType` | `string` | Specifies that the image or disk that is being used was licensed on-premises. &lt;br&gt;&lt;br&gt; Possible values for Windows Server operating system are: &lt;br&gt;&lt;br&gt; Windows_Client &lt;br&gt;&lt;br&gt; Windows_Server &lt;br&gt;&lt;br&gt; Possible values for Linux Server operating system are: &lt;br&gt;&lt;br&gt; RHEL_BYOS (for RHEL) &lt;br&gt;&lt;br&gt; SLES_BYOS (for SUSE) &lt;br&gt;&lt;br&gt; For more information, see [Azure Hybrid Use Benefit for Windows Server](https://docs.microsoft.com/azure/virtual-machines/windows/hybrid-use-benefit-licensing) &lt;br&gt;&lt;br&gt; [Azure Hybrid Use Benefit for Linux Server](https://docs.microsoft.com/azure/virtual-machines/linux/azure-hybrid-benefit-linux) &lt;br&gt;&lt;br&gt; Minimum api-version: 2015-06-15 |
| `osProfile` | `object` | Specifies the operating system settings for the virtual machine. Some of the settings cannot be changed once VM is provisioned. |
| `plan` | `object` | Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started -&gt;**. Enter any required information and then click **Save**. |
| `type` | `string` | Resource type |
| `location` | `string` | Resource location |
| `tags` | `object` | Resource tags |
| `instanceView` | `object` | The instance view of a virtual machine scale set VM. |
| `availabilitySet` | `object` |  |
| `networkProfileConfiguration` | `object` | Describes a virtual machine scale set VM network profile. |
| `userData` | `string` | UserData for the VM, which must be base-64 encoded. Customer should not pass any secrets in here. &lt;br&gt;&lt;br&gt;Minimum api-version: 2021-03-01 |
| `protectionPolicy` | `object` | The protection policy of a virtual machine scale set VM. |
| `vmId` | `string` | Azure VM unique ID. |
| `sku` | `object` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |
| `instanceId` | `string` | The virtual machine instance ID. |
| `resources` | `array` | The virtual machine child extension resources. |
| `diagnosticsProfile` | `object` | Specifies the boot diagnostic settings state. &lt;br&gt;&lt;br&gt;Minimum api-version: 2015-06-15. |
| `additionalCapabilities` | `object` | Enables or disables a capability on the virtual machine or virtual machine scale set. |
| `securityProfile` | `object` | Specifies the Security profile settings for the virtual machine or virtual machine scale set. |
| `latestModelApplied` | `boolean` | Specifies whether the latest model has been applied to the virtual machine. |
| `identity` | `object` | Identity for the virtual machine. |
| `hardwareProfile` | `object` | Specifies the hardware settings for the virtual machine. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachineScaleSetVMs_List` | `SELECT` | `resourceGroupName, subscriptionId, virtualMachineScaleSetName` | Gets a list of all virtual machines in a VM scale sets. |
| `VirtualMachineScaleSetVMs_Delete` | `DELETE` | `instanceId, resourceGroupName, subscriptionId, vmScaleSetName` | Deletes a virtual machine from a VM scale set. |
| `VirtualMachineScaleSetVMs_Deallocate` | `EXEC` | `instanceId, resourceGroupName, subscriptionId, vmScaleSetName` | Deallocates a specific virtual machine in a VM scale set. Shuts down the virtual machine and releases the compute resources it uses. You are not billed for the compute resources of this virtual machine once it is deallocated. |
| `VirtualMachineScaleSetVMs_Get` | `EXEC` | `instanceId, resourceGroupName, subscriptionId, vmScaleSetName` | Gets a virtual machine from a VM scale set. |
| `VirtualMachineScaleSetVMs_GetInstanceView` | `EXEC` | `instanceId, resourceGroupName, subscriptionId, vmScaleSetName` | Gets the status of a virtual machine from a VM scale set. |
| `VirtualMachineScaleSetVMs_PerformMaintenance` | `EXEC` | `instanceId, resourceGroupName, subscriptionId, vmScaleSetName` | Performs maintenance on a virtual machine in a VM scale set. |
| `VirtualMachineScaleSetVMs_PowerOff` | `EXEC` | `instanceId, resourceGroupName, subscriptionId, vmScaleSetName` | Power off (stop) a virtual machine in a VM scale set. Note that resources are still attached and you are getting charged for the resources. Instead, use deallocate to release resources and avoid charges. |
| `VirtualMachineScaleSetVMs_Redeploy` | `EXEC` | `instanceId, resourceGroupName, subscriptionId, vmScaleSetName` | Shuts down the virtual machine in the virtual machine scale set, moves it to a new node, and powers it back on. |
| `VirtualMachineScaleSetVMs_Reimage` | `EXEC` | `instanceId, resourceGroupName, subscriptionId, vmScaleSetName` | Reimages (upgrade the operating system) a specific virtual machine in a VM scale set. |
| `VirtualMachineScaleSetVMs_ReimageAll` | `EXEC` | `instanceId, resourceGroupName, subscriptionId, vmScaleSetName` | Allows you to re-image all the disks ( including data disks ) in the a VM scale set instance. This operation is only supported for managed disks. |
| `VirtualMachineScaleSetVMs_Restart` | `EXEC` | `instanceId, resourceGroupName, subscriptionId, vmScaleSetName` | Restarts a virtual machine in a VM scale set. |
| `VirtualMachineScaleSetVMs_RetrieveBootDiagnosticsData` | `EXEC` | `instanceId, resourceGroupName, subscriptionId, vmScaleSetName` | The operation to retrieve SAS URIs of boot diagnostic logs for a virtual machine in a VM scale set. |
| `VirtualMachineScaleSetVMs_RunCommand` | `EXEC` | `instanceId, resourceGroupName, subscriptionId, vmScaleSetName, data__commandId` | Run command on a virtual machine in a VM scale set. |
| `VirtualMachineScaleSetVMs_SimulateEviction` | `EXEC` | `instanceId, resourceGroupName, subscriptionId, vmScaleSetName` | The operation to simulate the eviction of spot virtual machine in a VM scale set. |
| `VirtualMachineScaleSetVMs_Start` | `EXEC` | `instanceId, resourceGroupName, subscriptionId, vmScaleSetName` | Starts a virtual machine in a VM scale set. |
| `VirtualMachineScaleSetVMs_Update` | `EXEC` | `instanceId, resourceGroupName, subscriptionId, vmScaleSetName` | Updates a virtual machine of a VM scale set. |
