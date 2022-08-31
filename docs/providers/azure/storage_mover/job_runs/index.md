---
title: job_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - job_runs
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
<tr><td><b>Name</b></td><td><code>job_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_mover.job_runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `executionStartTime` | `string` | Start time of the run. Null if no Agent reported that the job has started. |
| `targetProperties` | `object` | Copy of Endpoint resource's properties at time of Job Run creation. |
| `bytesExcluded` | `integer` | Bytes of data that will not be transferred, as they are excluded by user configuration. |
| `bytesTransferred` | `integer` | Bytes of data successfully transferred to target. |
| `scanStatus` | `string` | The status of Agent's scanning of source. |
| `itemsExcluded` | `integer` | Number of items that will not be transferred, as they are excluded by user configuration. |
| `error` | `object` | Error type |
| `executionEndTime` | `string` | End time of the run. Null if Agent has not reported that the job has ended. |
| `targetName` | `string` | Name of target Endpoint resource. This resource may no longer exist. |
| `itemsFailed` | `integer` | Number of items that were attempted to transfer and failed. |
| `sourceName` | `string` | Name of source Endpoint resource. This resource may no longer exist. |
| `provisioningState` | `string` | The provisioning state of this resource. |
| `bytesNoTransferNeeded` | `integer` | Bytes of data that will not be transferred, as they are already found on target (e.g. mirror mode). |
| `status` | `string` | The state of the job execution. |
| `bytesUnsupported` | `integer` | Bytes of data that will not be transferred, as they are unsupported on target. |
| `sourceResourceId` | `string` | Fully qualified resource id of source Endpoint. This id may no longer exist. |
| `itemsScanned` | `integer` | Number of items scanned so far in source. |
| `agentName` | `string` | Name of the Agent assigned to this run. |
| `jobDefinitionProperties` | `object` | Copy of parent Job Definition's properties at time of Job Run creation. |
| `bytesFailed` | `integer` | Bytes of data that were attempted to transfer and failed. |
| `itemsUnsupported` | `integer` | Number of items that will not be transferred, as they are unsupported on target. |
| `targetResourceId` | `string` | Fully qualified resource id of of Endpoint. This id may no longer exist. |
| `itemsTransferred` | `integer` | Number of items successfully transferred to target. |
| `lastStatusUpdate` | `string` | The last updated time of the Job Run. |
| `itemsNoTransferNeeded` | `integer` | Number of items that will not be transferred, as they are already found on target (e.g. mirror mode). |
| `bytesScanned` | `integer` | Bytes of data scanned so far in source. |
| `agentResourceId` | `string` | Fully qualified resource id of the Agent assigned to this run. |
| `sourceProperties` | `object` | Copy of source Endpoint resource's properties at time of Job Run creation. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `JobRuns_List` | `SELECT` | `jobDefinitionName, projectName, resourceGroupName, storageMoverName, subscriptionId` | Lists all Job Runs in a Job Definition. |
| `JobRuns_Get` | `EXEC` | `jobDefinitionName, jobRunName, projectName, resourceGroupName, storageMoverName, subscriptionId` | Gets a Job Run resource. |
