---
title: registered_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - registered_servers
  - storage_sync
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
<tr><td><b>Name</b></td><td><code>registered_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_sync.registered_servers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `monitoringEndpointUri` | `string` | Telemetry Endpoint Uri |
| `serverOSVersion` | `string` | Registered Server OS Version |
| `serviceLocation` | `string` | Service Location |
| `agentVersionStatus` | `string` | Type of the registered server agent version status |
| `lastWorkflowId` | `string` | Registered Server lastWorkflowId |
| `provisioningState` | `string` | Registered Server Provisioning State |
| `agentVersion` | `string` | Registered Server Agent Version |
| `serverCertificate` | `string` | Registered Server Certificate |
| `managementEndpointUri` | `string` | Management Endpoint Uri |
| `agentVersionExpirationDate` | `string` | Registered Server Agent Version Expiration Date |
| `storageSyncServiceUid` | `string` | Registered Server storageSyncServiceUid |
| `friendlyName` | `string` | Friendly Name |
| `monitoringConfiguration` | `string` | Monitoring Configuration |
| `clusterName` | `string` | Registered Server clusterName |
| `clusterId` | `string` | Registered Server clusterId |
| `serverManagementErrorCode` | `integer` | Registered Server Management Error Code |
| `resourceLocation` | `string` | Resource Location |
| `serverId` | `string` | Registered Server serverId |
| `lastHeartBeat` | `string` | Registered Server last heart beat |
| `lastOperationName` | `string` | Resource Last Operation Name |
| `discoveryEndpointUri` | `string` | Resource discoveryEndpointUri |
| `serverName` | `string` | Server name |
| `serverRole` | `string` | Registered Server serverRole |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RegisteredServers_ListByStorageSyncService` | `SELECT` | `resourceGroupName, storageSyncServiceName, subscriptionId` | Get a given registered server list. |
| `RegisteredServers_Create` | `INSERT` | `resourceGroupName, serverId, storageSyncServiceName, subscriptionId` | Add a new registered server. |
| `RegisteredServers_Delete` | `DELETE` | `resourceGroupName, serverId, storageSyncServiceName, subscriptionId` | Delete the given registered server. |
| `RegisteredServers_Get` | `EXEC` | `resourceGroupName, serverId, storageSyncServiceName, subscriptionId` | Get a given registered server. |
| `RegisteredServers_triggerRollover` | `EXEC` | `resourceGroupName, serverId, storageSyncServiceName, subscriptionId` | Triggers Server certificate rollover. |
