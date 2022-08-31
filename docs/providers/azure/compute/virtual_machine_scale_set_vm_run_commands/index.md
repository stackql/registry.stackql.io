---
title: virtual_machine_scale_set_vm_run_commands
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_set_vm_run_commands
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
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_set_vm_run_commands</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machine_scale_set_vm_run_commands</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `location` | `string` | Resource location |
| `type` | `string` | Resource type |
| `runAsPassword` | `string` | Specifies the user account password on the VM when executing the run command. |
| `outputBlobUri` | `string` | Specifies the Azure storage blob where script output stream will be uploaded. |
| `tags` | `object` | Resource tags |
| `provisioningState` | `string` | The provisioning state, which only appears in the response. |
| `asyncExecution` | `boolean` | Optional. If set to true, provisioning will complete as soon as the script starts and will not wait for script to complete. |
| `runAsUser` | `string` | Specifies the user account on the VM when executing the run command. |
| `errorBlobUri` | `string` | Specifies the Azure storage blob where script error stream will be uploaded. |
| `parameters` | `array` | The parameters used by the script. |
| `protectedParameters` | `array` | The parameters used by the script. |
| `timeoutInSeconds` | `integer` | The timeout in seconds to execute the run command. |
| `source` | `object` | Describes the script sources for run command. |
| `instanceView` | `object` | The instance view of a virtual machine run command. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachineScaleSetVMRunCommands_List` | `SELECT` | `instanceId, resourceGroupName, subscriptionId, vmScaleSetName` | The operation to get all run commands of an instance in Virtual Machine Scaleset. |
| `VirtualMachineScaleSetVMRunCommands_CreateOrUpdate` | `INSERT` | `instanceId, resourceGroupName, runCommandName, subscriptionId, vmScaleSetName` | The operation to create or update the VMSS VM run command. |
| `VirtualMachineScaleSetVMRunCommands_Delete` | `DELETE` | `instanceId, resourceGroupName, runCommandName, subscriptionId, vmScaleSetName` | The operation to delete the VMSS VM run command. |
| `VirtualMachineScaleSetVMRunCommands_Get` | `EXEC` | `instanceId, resourceGroupName, runCommandName, subscriptionId, vmScaleSetName` | The operation to get the VMSS VM run command. |
| `VirtualMachineScaleSetVMRunCommands_Update` | `EXEC` | `instanceId, resourceGroupName, runCommandName, subscriptionId, vmScaleSetName` | The operation to update the VMSS VM run command. |
