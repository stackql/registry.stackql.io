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
| `managementEndpointUri` | `string` | Management Endpoint Uri |
| `agentVersionExpirationDate` | `string` | Registered Server Agent Version Expiration Date |
| `lastOperationName` | `string` | Resource Last Operation Name |
| `agentVersionStatus` | `string` | Type of the registered server agent version status |
| `serverName` | `string` | Server name |
| `serverManagementErrorCode` | `integer` | Registered Server Management Error Code |
| `lastHeartBeat` | `string` | Registered Server last heart beat |
| `clusterName` | `string` | Registered Server clusterName |
| `clusterId` | `string` | Registered Server clusterId |
| `serverCertificate` | `string` | Registered Server Certificate |
| `monitoringConfiguration` | `string` | Monitoring Configuration |
| `serviceLocation` | `string` | Service Location |
| `discoveryEndpointUri` | `string` | Resource discoveryEndpointUri |
| `agentVersion` | `string` | Registered Server Agent Version |
| `lastWorkflowId` | `string` | Registered Server lastWorkflowId |
| `monitoringEndpointUri` | `string` | Telemetry Endpoint Uri |
| `provisioningState` | `string` | Registered Server Provisioning State |
| `resourceLocation` | `string` | Resource Location |
| `serverOSVersion` | `string` | Registered Server OS Version |
| `friendlyName` | `string` | Friendly Name |
| `serverId` | `string` | Registered Server serverId |
| `serverRole` | `string` | Registered Server serverRole |
| `storageSyncServiceUid` | `string` | Registered Server storageSyncServiceUid |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RegisteredServers_ListByStorageSyncService` | `SELECT` | `resourceGroupName, storageSyncServiceName, subscriptionId` | Get a given registered server list. |
| `RegisteredServers_Create` | `INSERT` | `resourceGroupName, serverId, storageSyncServiceName, subscriptionId` | Add a new registered server. |
| `RegisteredServers_Delete` | `DELETE` | `resourceGroupName, serverId, storageSyncServiceName, subscriptionId` | Delete the given registered server. |
| `RegisteredServers_Get` | `EXEC` | `resourceGroupName, serverId, storageSyncServiceName, subscriptionId` | Get a given registered server. |
| `RegisteredServers_triggerRollover` | `EXEC` | `resourceGroupName, serverId, storageSyncServiceName, subscriptionId` | Triggers Server certificate rollover. |
