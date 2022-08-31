---
title: virtual_machine_scale_set_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_set_extensions
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
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_set_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machine_scale_set_extensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | The name of the extension. |
| `protectedSettingsFromKeyVault` | `object` | The extensions protected settings that are passed by reference, and consumed from key vault |
| `typeHandlerVersion` | `string` | Specifies the version of the script handler. |
| `provisionAfterExtensions` | `array` | Collection of extension names after which this extension needs to be provisioned. |
| `enableAutomaticUpgrade` | `boolean` | Indicates whether the extension should be automatically upgraded by the platform if there is a newer version of the extension available. |
| `provisioningState` | `string` | The provisioning state, which only appears in the response. |
| `forceUpdateTag` | `string` | If a value is provided and is different from the previous value, the extension handler will be forced to update even if the extension configuration has not changed. |
| `settings` | `object` | Json formatted public settings for the extension. |
| `publisher` | `string` | The name of the extension handler publisher. |
| `type` | `string` | Resource type |
| `suppressFailures` | `boolean` | Indicates whether failures stemming from the extension will be suppressed (Operational failures such as not connecting to the VM will not be suppressed regardless of this value). The default is false. |
| `autoUpgradeMinorVersion` | `boolean` | Indicates whether the extension should use a newer minor version if one is available at deployment time. Once deployed, however, the extension will not upgrade minor versions unless redeployed, even with this property set to true. |
| `protectedSettings` | `object` | The extension can contain either protectedSettings or protectedSettingsFromKeyVault or no protected settings at all. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachineScaleSetExtensions_List` | `SELECT` | `resourceGroupName, subscriptionId, vmScaleSetName` | Gets a list of all extensions in a VM scale set. |
| `VirtualMachineScaleSetExtensions_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, vmScaleSetName, vmssExtensionName` | The operation to create or update an extension. |
| `VirtualMachineScaleSetExtensions_Delete` | `DELETE` | `resourceGroupName, subscriptionId, vmScaleSetName, vmssExtensionName` | The operation to delete the extension. |
| `VirtualMachineScaleSetExtensions_Get` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName, vmssExtensionName` | The operation to get the extension. |
| `VirtualMachineScaleSetExtensions_Update` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName, vmssExtensionName` | The operation to update an extension. |
