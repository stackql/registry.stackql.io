---
title: virtual_machine_run_commands
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_run_commands
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
<tr><td><b>Name</b></td><td><code>virtual_machine_run_commands</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machine_run_commands</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `type` | `string` | Resource type |
| `outputBlobUri` | `string` | Specifies the Azure storage blob where script output stream will be uploaded. |
| `asyncExecution` | `boolean` | Optional. If set to true, provisioning will complete as soon as the script starts and will not wait for script to complete. |
| `tags` | `object` | Resource tags |
| `location` | `string` | Resource location |
| `protectedParameters` | `array` | The parameters used by the script. |
| `parameters` | `array` | The parameters used by the script. |
| `provisioningState` | `string` | The provisioning state, which only appears in the response. |
| `instanceView` | `object` | The instance view of a virtual machine run command. |
| `source` | `object` | Describes the script sources for run command. |
| `runAsPassword` | `string` | Specifies the user account password on the VM when executing the run command. |
| `errorBlobUri` | `string` | Specifies the Azure storage blob where script error stream will be uploaded. |
| `timeoutInSeconds` | `integer` | The timeout in seconds to execute the run command. |
| `runAsUser` | `string` | Specifies the user account on the VM when executing the run command. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachineRunCommands_List` | `SELECT` | `location, subscriptionId` | Lists all available run commands for a subscription in a location. |
| `VirtualMachineRunCommands_ListByVirtualMachine` | `SELECT` | `resourceGroupName, subscriptionId, vmName` | The operation to get all run commands of a Virtual Machine. |
| `VirtualMachineRunCommands_CreateOrUpdate` | `INSERT` | `resourceGroupName, runCommandName, subscriptionId, vmName` | The operation to create or update the run command. |
| `VirtualMachineRunCommands_Delete` | `DELETE` | `resourceGroupName, runCommandName, subscriptionId, vmName` | The operation to delete the run command. |
| `VirtualMachineRunCommands_Get` | `EXEC` | `commandId, location, subscriptionId` | Gets specific run command for a subscription in a location. |
| `VirtualMachineRunCommands_GetByVirtualMachine` | `EXEC` | `resourceGroupName, runCommandName, subscriptionId, vmName` | The operation to get the run command. |
| `VirtualMachineRunCommands_Update` | `EXEC` | `resourceGroupName, runCommandName, subscriptionId, vmName` | The operation to update the run command. |
