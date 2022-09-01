---
title: virtual_machine_scale_set_vm_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_set_vm_extensions
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
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_set_vm_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machine_scale_set_vm_extensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | The name of the extension. |
| `forceUpdateTag` | `string` | How the extension handler should be forced to update even if the extension configuration has not changed. |
| `protectedSettings` | `object` | The extension can contain either protectedSettings or protectedSettingsFromKeyVault or no protected settings at all. |
| `suppressFailures` | `boolean` | Indicates whether failures stemming from the extension will be suppressed (Operational failures such as not connecting to the VM will not be suppressed regardless of this value). The default is false. |
| `typeHandlerVersion` | `string` | Specifies the version of the script handler. |
| `instanceView` | `object` | The instance view of a virtual machine extension. |
| `autoUpgradeMinorVersion` | `boolean` | Indicates whether the extension should use a newer minor version if one is available at deployment time. Once deployed, however, the extension will not upgrade minor versions unless redeployed, even with this property set to true. |
| `type` | `string` | Resource type |
| `protectedSettingsFromKeyVault` | `object` | The extensions protected settings that are passed by reference, and consumed from key vault |
| `settings` | `object` | Json formatted public settings for the extension. |
| `publisher` | `string` | The name of the extension handler publisher. |
| `provisioningState` | `string` | The provisioning state, which only appears in the response. |
| `enableAutomaticUpgrade` | `boolean` | Indicates whether the extension should be automatically upgraded by the platform if there is a newer version of the extension available. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachineScaleSetVMExtensions_List` | `SELECT` | `instanceId, resourceGroupName, subscriptionId, vmScaleSetName` | The operation to get all extensions of an instance in Virtual Machine Scaleset. |
| `VirtualMachineScaleSetVMExtensions_CreateOrUpdate` | `INSERT` | `instanceId, resourceGroupName, subscriptionId, vmExtensionName, vmScaleSetName` | The operation to create or update the VMSS VM extension. |
| `VirtualMachineScaleSetVMExtensions_Delete` | `DELETE` | `instanceId, resourceGroupName, subscriptionId, vmExtensionName, vmScaleSetName` | The operation to delete the VMSS VM extension. |
| `VirtualMachineScaleSetVMExtensions_Get` | `EXEC` | `instanceId, resourceGroupName, subscriptionId, vmExtensionName, vmScaleSetName` | The operation to get the VMSS VM extension. |
| `VirtualMachineScaleSetVMExtensions_Update` | `EXEC` | `instanceId, resourceGroupName, subscriptionId, vmExtensionName, vmScaleSetName` | The operation to update the VMSS VM extension. |
