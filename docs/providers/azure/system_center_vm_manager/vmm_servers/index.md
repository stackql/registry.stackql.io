---
title: vmm_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - vmm_servers
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
<tr><td><b>Name</b></td><td><code>vmm_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.system_center_vm_manager.vmm_servers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `connectionStatus` | `string` | Gets or sets the connection status to the vmmServer. |
| `provisioningState` | `string` | Gets or sets the provisioning state. |
| `location` | `string` | Gets or sets the location. |
| `errorMessage` | `string` | Gets or sets any error message if connection to vmmServer is having any issue. |
| `port` | `integer` | Port is the port on which the vmmServer is listening. |
| `fqdn` | `string` | Fqdn is the hostname/ip of the vmmServer. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `extendedLocation` | `object` | The extended location. |
| `version` | `string` | Version is the version of the vmmSever. |
| `tags` | `object` | Resource tags |
| `uuid` | `string` | Unique ID of vmmServer. |
| `type` | `string` | Resource Type |
| `credentials` | `object` | Credentials to connect to VMMServer. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VmmServers_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List of VmmServers in a resource group. |
| `VmmServers_ListBySubscription` | `SELECT` | `subscriptionId` | List of VmmServers in a subscription. |
| `VmmServers_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, vmmServerName, data__extendedLocation, data__location` | Onboards the SCVMM fabric as an Azure VmmServer resource. |
| `VmmServers_Delete` | `DELETE` | `resourceGroupName, subscriptionId, vmmServerName` | Deboards the SCVMM fabric from Azure. |
| `VmmServers_Get` | `EXEC` | `resourceGroupName, subscriptionId, vmmServerName` | Implements VMMServer GET method. |
| `VmmServers_Update` | `EXEC` | `resourceGroupName, subscriptionId, vmmServerName` | Updates the VmmServers resource. |
