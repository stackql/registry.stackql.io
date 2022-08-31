---
title: runs
hide_title: false
hide_table_of_contents: false
keywords:
  - runs
  - container_registry
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
<tr><td><b>Name</b></td><td><code>runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `runType` | `string` | The type of run. |
| `status` | `string` | The current status of the run. |
| `agentConfiguration` | `object` | The properties that determine the run agent configuration. |
| `runId` | `string` | The unique identifier for the run. |
| `isArchiveEnabled` | `boolean` | The value that indicates whether archiving is enabled or not. |
| `lastUpdatedTime` | `string` | The last updated time for the run. |
| `runErrorMessage` | `string` | The error message received from backend systems after the run is scheduled. |
| `task` | `string` | The task against which run was scheduled. |
| `outputImages` | `array` | The list of all images that were generated from the run. This is applicable if the run generates base image dependencies. |
| `type` | `string` | The type of the resource. |
| `agentPoolName` | `string` | The dedicated agent pool for the run. |
| `customRegistries` | `array` | The list of custom registries that were logged in during this run. |
| `imageUpdateTrigger` | `object` | The image update trigger that caused a build. |
| `timerTrigger` | `object` |  |
| `updateTriggerToken` | `string` | The update trigger token passed for the Run. |
| `createTime` | `string` | The time the run was scheduled. |
| `finishTime` | `string` | The time the run finished. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `platform` | `object` | The platform properties against which the run has to happen. |
| `sourceTrigger` | `object` | The source trigger that caused a run. |
| `sourceRegistryAuth` | `string` | The scope of the credentials that were used to login to the source registry during this run. |
| `provisioningState` | `string` | The provisioning state of a run. |
| `logArtifact` | `object` | Properties for a registry image. |
| `startTime` | `string` | The time the run started. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Runs_List` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Gets all the runs for a registry. |
| `Runs_Cancel` | `EXEC` | `registryName, resourceGroupName, runId, subscriptionId` | Cancel an existing run. |
| `Runs_Get` | `EXEC` | `registryName, resourceGroupName, runId, subscriptionId` | Gets the detailed information for a given run. |
| `Runs_GetLogSasUrl` | `EXEC` | `registryName, resourceGroupName, runId, subscriptionId` | Gets a link to download the run logs. |
| `Runs_Update` | `EXEC` | `registryName, resourceGroupName, runId, subscriptionId` | Patch the run properties. |
