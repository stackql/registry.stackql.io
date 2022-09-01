---
title: agents
hide_title: false
hide_table_of_contents: false
keywords:
  - agents
  - storage_mover
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
<tr><td><b>Name</b></td><td><code>agents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_mover.agents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | A description for the Agent. |
| `errorDetails` | `object` |  |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `provisioningState` | `string` | The provisioning state of this resource. |
| `uptimeInSeconds` | `integer` | Uptime of the Agent in seconds. |
| `arcResourceId` | `string` | The fully qualified resource ID of the Hybrid Compute resource for the Agent. |
| `agentVersion` | `string` | The Agent version. |
| `arcVmUuid` | `string` | The VM UUID of the Hybrid Compute resource for the Agent. |
| `lastStatusUpdate` | `string` | The last updated time of the Agent status. |
| `localIPAddress` | `string` | Local IP address reported by the Agent. |
| `numberOfCores` | `integer` | Available compute cores reported by the Agent. |
| `memoryInMB` | `integer` | Available memory reported by the Agent, in MB. |
| `agentStatus` | `string` | The Agent status. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Agents_List` | `SELECT` | `resourceGroupName, storageMoverName, subscriptionId` | Lists all Agents in a Storage Mover. |
| `Agents_CreateOrUpdate` | `INSERT` | `agentName, resourceGroupName, storageMoverName, subscriptionId` | Creates or updates an Agent resource, which references a hybrid compute machine that can run jobs. |
| `Agents_Delete` | `DELETE` | `agentName, resourceGroupName, storageMoverName, subscriptionId` | Deletes an Agent resource. |
| `Agents_Get` | `EXEC` | `agentName, resourceGroupName, storageMoverName, subscriptionId` | Gets an Agent resource. |
| `Agents_Update` | `EXEC` | `agentName, resourceGroupName, storageMoverName, subscriptionId` | Creates or updates an Agent resource. |
