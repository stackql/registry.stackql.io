---
title: virtual_machine_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_extensions
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
<tr><td><b>Name</b></td><td><code>virtual_machine_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machine_extensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `forceUpdateTag` | `string` | How the extension handler should be forced to update even if the extension configuration has not changed. |
| `settings` | `object` | Json formatted public settings for the extension. |
| `location` | `string` | Resource location |
| `instanceView` | `object` | The instance view of a virtual machine extension. |
| `provisioningState` | `string` | The provisioning state, which only appears in the response. |
| `tags` | `object` | Resource tags |
| `autoUpgradeMinorVersion` | `boolean` | Indicates whether the extension should use a newer minor version if one is available at deployment time. Once deployed, however, the extension will not upgrade minor versions unless redeployed, even with this property set to true. |
| `suppressFailures` | `boolean` | Indicates whether failures stemming from the extension will be suppressed (Operational failures such as not connecting to the VM will not be suppressed regardless of this value). The default is false. |
| `type` | `string` | Resource type |
| `protectedSettings` | `object` | The extension can contain either protectedSettings or protectedSettingsFromKeyVault or no protected settings at all. |
| `enableAutomaticUpgrade` | `boolean` | Indicates whether the extension should be automatically upgraded by the platform if there is a newer version of the extension available. |
| `protectedSettingsFromKeyVault` | `object` | The extensions protected settings that are passed by reference, and consumed from key vault |
| `publisher` | `string` | The name of the extension handler publisher. |
| `typeHandlerVersion` | `string` | Specifies the version of the script handler. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachineExtensions_List` | `SELECT` | `resourceGroupName, subscriptionId, vmName` | The operation to get all extensions of a Virtual Machine. |
| `VirtualMachineExtensions_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, vmExtensionName, vmName` | The operation to create or update the extension. |
| `VirtualMachineExtensions_Delete` | `DELETE` | `resourceGroupName, subscriptionId, vmExtensionName, vmName` | The operation to delete the extension. |
| `VirtualMachineExtensions_Get` | `EXEC` | `resourceGroupName, subscriptionId, vmExtensionName, vmName` | The operation to get the extension. |
| `VirtualMachineExtensions_Update` | `EXEC` | `resourceGroupName, subscriptionId, vmExtensionName, vmName` | The operation to update the extension. |
