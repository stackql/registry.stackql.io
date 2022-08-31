---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
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
<tr><td><b>Name</b></td><td><code>virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `host` | `object` |  |
| `resources` | `array` | The virtual machine child extension resources. |
| `proximityPlacementGroup` | `object` |  |
| `instanceView` | `object` | The instance view of a virtual machine. |
| `timeCreated` | `string` | Specifies the time at which the Virtual Machine resource was created.&lt;br&gt;&lt;br&gt;Minimum api-version: 2022-03-01. |
| `priority` | `string` | Specifies the priority for a standalone virtual machine or the virtual machines in the scale set. &lt;br&gt;&lt;br&gt; 'Low' enum will be deprecated in the future, please use 'Spot' as the enum to deploy Azure Spot VM/VMSS. |
| `applicationProfile` | `object` | Contains the list of gallery applications that should be made available to the VM/VMSS |
| `availabilitySet` | `object` |  |
| `provisioningState` | `string` | The provisioning state, which only appears in the response. |
| `extensionsTimeBudget` | `string` | Specifies the time alloted for all extensions to start. The time duration should be between 15 minutes and 120 minutes (inclusive) and should be specified in ISO 8601 format. The default value is 90 minutes (PT1H30M). &lt;br&gt;&lt;br&gt; Minimum api-version: 2020-06-01 |
| `scheduledEventsProfile` | `object` |  |
| `billingProfile` | `object` | Specifies the billing related details of a Azure Spot VM or VMSS. &lt;br&gt;&lt;br&gt;Minimum api-version: 2019-03-01. |
| `osProfile` | `object` | Specifies the operating system settings for the virtual machine. Some of the settings cannot be changed once VM is provisioned. |
| `extendedLocation` | `object` | The complex type of the extended location. |
| `storageProfile` | `object` | Specifies the storage settings for the virtual machine disks. |
| `tags` | `object` | Resource tags |
| `userData` | `string` | UserData for the VM, which must be base-64 encoded. Customer should not pass any secrets in here. &lt;br&gt;&lt;br&gt;Minimum api-version: 2021-03-01 |
| `platformFaultDomain` | `integer` | Specifies the scale set logical fault domain into which the Virtual Machine will be created. By default, the Virtual Machine will by automatically assigned to a fault domain that best maintains balance across available fault domains.&lt;br&gt;&lt;li&gt;This is applicable only if the 'virtualMachineScaleSet' property of this Virtual Machine is set.&lt;li&gt;The Virtual Machine Scale Set that is referenced, must have 'platformFaultDomainCount' &gt; 1.&lt;li&gt;This property cannot be updated once the Virtual Machine is created.&lt;li&gt;Fault domain assignment can be viewed in the Virtual Machine Instance View.&lt;br&gt;&lt;br&gt;Minimum api‐version: 2020‐12‐01 |
| `capacityReservation` | `object` | The parameters of a capacity reservation Profile. |
| `hostGroup` | `object` |  |
| `vmId` | `string` | Specifies the VM unique ID which is a 128-bits identifier that is encoded and stored in all Azure IaaS VMs SMBIOS and can be read using platform BIOS commands. |
| `evictionPolicy` | `string` | Specifies the eviction policy for the Azure Spot VM/VMSS |
| `licenseType` | `string` | Specifies that the image or disk that is being used was licensed on-premises. &lt;br&gt;&lt;br&gt; Possible values for Windows Server operating system are: &lt;br&gt;&lt;br&gt; Windows_Client &lt;br&gt;&lt;br&gt; Windows_Server &lt;br&gt;&lt;br&gt; Possible values for Linux Server operating system are: &lt;br&gt;&lt;br&gt; RHEL_BYOS (for RHEL) &lt;br&gt;&lt;br&gt; SLES_BYOS (for SUSE) &lt;br&gt;&lt;br&gt; For more information, see [Azure Hybrid Use Benefit for Windows Server](https://docs.microsoft.com/azure/virtual-machines/windows/hybrid-use-benefit-licensing) &lt;br&gt;&lt;br&gt; [Azure Hybrid Use Benefit for Linux Server](https://docs.microsoft.com/azure/virtual-machines/linux/azure-hybrid-benefit-linux) &lt;br&gt;&lt;br&gt; Minimum api-version: 2015-06-15 |
| `plan` | `object` | Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started -&gt;**. Enter any required information and then click **Save**. |
| `diagnosticsProfile` | `object` | Specifies the boot diagnostic settings state. &lt;br&gt;&lt;br&gt;Minimum api-version: 2015-06-15. |
| `type` | `string` | Resource type |
| `location` | `string` | Resource location |
| `additionalCapabilities` | `object` | Enables or disables a capability on the virtual machine or virtual machine scale set. |
| `networkProfile` | `object` | Specifies the network interfaces or the networking configuration of the virtual machine. |
| `zones` | `array` | The virtual machine zones. |
| `hardwareProfile` | `object` | Specifies the hardware settings for the virtual machine. |
| `virtualMachineScaleSet` | `object` |  |
| `identity` | `object` | Identity for the virtual machine. |
| `securityProfile` | `object` | Specifies the Security profile settings for the virtual machine or virtual machine scale set. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachines_List` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all of the virtual machines in the specified resource group. Use the nextLink property in the response to get the next page of virtual machines. |
| `VirtualMachines_ListAll` | `SELECT` | `subscriptionId` | Lists all of the virtual machines in the specified subscription. Use the nextLink property in the response to get the next page of virtual machines. |
| `VirtualMachines_ListByLocation` | `SELECT` | `location, subscriptionId` | Gets all the virtual machines under the specified subscription for the specified location. |
| `VirtualMachines_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, vmName` | The operation to create or update a virtual machine. Please note some properties can be set only during virtual machine creation. |
| `VirtualMachines_Delete` | `DELETE` | `resourceGroupName, subscriptionId, vmName` | The operation to delete a virtual machine. |
| `VirtualMachines_AssessPatches` | `EXEC` | `resourceGroupName, subscriptionId, vmName` | Assess patches on the VM. |
| `VirtualMachines_Capture` | `EXEC` | `resourceGroupName, subscriptionId, vmName, data__destinationContainerName, data__overwriteVhds, data__vhdPrefix` | Captures the VM by copying virtual hard disks of the VM and outputs a template that can be used to create similar VMs. |
| `VirtualMachines_ConvertToManagedDisks` | `EXEC` | `resourceGroupName, subscriptionId, vmName` | Converts virtual machine disks from blob-based to managed disks. Virtual machine must be stop-deallocated before invoking this operation. |
| `VirtualMachines_Deallocate` | `EXEC` | `resourceGroupName, subscriptionId, vmName` | Shuts down the virtual machine and releases the compute resources. You are not billed for the compute resources that this virtual machine uses. |
| `VirtualMachines_Generalize` | `EXEC` | `resourceGroupName, subscriptionId, vmName` | Sets the OS state of the virtual machine to generalized. It is recommended to sysprep the virtual machine before performing this operation. &lt;br&gt;For Windows, please refer to [Create a managed image of a generalized VM in Azure](https://docs.microsoft.com/azure/virtual-machines/windows/capture-image-resource).&lt;br&gt;For Linux, please refer to [How to create an image of a virtual machine or VHD](https://docs.microsoft.com/azure/virtual-machines/linux/capture-image). |
| `VirtualMachines_Get` | `EXEC` | `resourceGroupName, subscriptionId, vmName` | Retrieves information about the model view or the instance view of a virtual machine. |
| `VirtualMachines_InstallPatches` | `EXEC` | `resourceGroupName, subscriptionId, vmName, data__rebootSetting` | Installs patches on the VM. |
| `VirtualMachines_InstanceView` | `EXEC` | `resourceGroupName, subscriptionId, vmName` | Retrieves information about the run-time state of a virtual machine. |
| `VirtualMachines_ListAvailableSizes` | `EXEC` | `resourceGroupName, subscriptionId, vmName` | Lists all available virtual machine sizes to which the specified virtual machine can be resized. |
| `VirtualMachines_PerformMaintenance` | `EXEC` | `resourceGroupName, subscriptionId, vmName` | The operation to perform maintenance on a virtual machine. |
| `VirtualMachines_PowerOff` | `EXEC` | `resourceGroupName, subscriptionId, vmName` | The operation to power off (stop) a virtual machine. The virtual machine can be restarted with the same provisioned resources. You are still charged for this virtual machine. |
| `VirtualMachines_Reapply` | `EXEC` | `resourceGroupName, subscriptionId, vmName` | The operation to reapply a virtual machine's state. |
| `VirtualMachines_Redeploy` | `EXEC` | `resourceGroupName, subscriptionId, vmName` | Shuts down the virtual machine, moves it to a new node, and powers it back on. |
| `VirtualMachines_Reimage` | `EXEC` | `resourceGroupName, subscriptionId, vmName` | Reimages the virtual machine which has an ephemeral OS disk back to its initial state. |
| `VirtualMachines_Restart` | `EXEC` | `resourceGroupName, subscriptionId, vmName` | The operation to restart a virtual machine. |
| `VirtualMachines_RetrieveBootDiagnosticsData` | `EXEC` | `resourceGroupName, subscriptionId, vmName` | The operation to retrieve SAS URIs for a virtual machine's boot diagnostic logs. |
| `VirtualMachines_RunCommand` | `EXEC` | `resourceGroupName, subscriptionId, vmName, data__commandId` | Run command on the VM. |
| `VirtualMachines_SimulateEviction` | `EXEC` | `resourceGroupName, subscriptionId, vmName` | The operation to simulate the eviction of spot virtual machine. |
| `VirtualMachines_Start` | `EXEC` | `resourceGroupName, subscriptionId, vmName` | The operation to start a virtual machine. |
| `VirtualMachines_Update` | `EXEC` | `resourceGroupName, subscriptionId, vmName` | The operation to update a virtual machine. |